import os.path
import base64
import email

# For Google APIs
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# For command line arguments
import argparse
parser = argparse.ArgumentParser(description="Gmail Helper", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--action", choices={"send","search","none"}, default="none", help="Send Email, Search Email, Do nothing")
parser.add_argument("-e", action='store', type=str, help="Recipient email address")
parser.add_argument("-s", action='store', type=str, default="",help="Subject line")
parser.add_argument("-b", action='store', type=str, default="",help="Email body")
parser.add_argument("-k", action='store', type=str, help="Search keyword")

args = parser.parse_args()
action = args.action
recipient = args.e
subject = args.s
body = args.b
keyword = args.k


### If modifying these scopes, delete the file token.json. ###
SCOPES = ['https://mail.google.com/']


class MyGmail:
    def __init__(self):
        """
        Authenticate the google api client and return the service object 
        to make further calls

        Args:
            None
        Returns:
            service api object from Gmail for making calls
        """
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())
    
        # Call the Gmail API        
        self.service = build('gmail', 'v1', credentials=self.creds)


    def send_email(self, receiver, subject, body):
        """Create and send an email message
        Print the sent message id

        Args:
            receiver: receiver email
            subject: email subject
            body: email body

        Returns:
            send_email: Message object, including message id
        """
        try:
            message = email.message.EmailMessage()

            # receiver and subject
            message['To'] = receiver
            message['Subject'] = subject

            # message body
            message.set_content(body)

            # encoded message
            encoded_message = {
                'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
            }
            
            send_email = (self.service.users().messages().send(userId="me", body=encoded_message).execute())

        except HttpError as error:
            print(f'An error occurred: {error}')
            send_email = None

        return send_email


    def search_email(self, keyword):
        """
        Search the inbox for emails using standard gmail search parameters
        and return a list of email IDs for each result

        Args:
            keyword: search operators you can use with Gmail
            (see https://support.google.com/mail/answer/7190?hl=en for a list)

        Returns:
            list_ids: list containing email IDs of search query
        """
        try:
            # initiate the list for returning
            list_ids = []

            # get the id of all messages that are in the search string
            search_ids = self.service.users().messages().list(userId='me', q=keyword).execute()
            
            # if there were no results, print warning and return empty string
            try:
                ids = search_ids['messages']
            except KeyError:
                print("WARNING: the search queried returned 0 results")
                print("returning an empty string")
                return ""

            # return list of message ids
            if len(ids)>1:
                for msg_id in ids:
                    list_ids.append(msg_id['id'])
                return(list_ids)
            else:
                list_ids = ids[0]['id']
                return [list_ids]
            
        except HttpError as error:
            print(f'An error in search_email occurred: {error}')


if __name__ == '__main__':

    # service object from the Gmail API
    service = MyGmail()
    
    if action == "send":         # send email
        sent_email = service.send_email(recipient, subject, body)
        print(f'Sent email: {sent_email}')
    elif action == "search":    # search emails
        emails_matched = service.search_email(keyword)
        if emails_matched:
            print("Number of emails with keyword '" + str(keyword) + "': " + str(len(emails_matched)))
            print("Email IDs: ", emails_matched)
    else:
        print("No action selected")

