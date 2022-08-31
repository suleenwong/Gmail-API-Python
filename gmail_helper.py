# For Google APIs
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path
import base64
import email
import time

# For command line compatibility
import argparse
parser = argparse.ArgumentParser(description="Gmail Helper")
parser.add_argument("--manual", action="store_true", default=False, help="specifies if the script is running in manual mode")
parser.add_argument("-o", choices={"email","search","none"}, default="none", help="Send Email, Search Email, Do Nothing")
parser.add_argument("-e", action='store', type=str, help="Email address of recipient")
parser.add_argument("-s", action='store', type=str, default="",help="Subject line")
parser.add_argument("-b", action='store', type=str, default="",help="Body of email")
parser.add_argument("-k", action='store', type=str, help="Search keyword")

args = parser.parse_args()
mode = args.manual
action = args.o
recipient = args.e
subject = args.s
body = args.b
keyword = args.k

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

# Email address which will be used to send emails
EMAIL = "testa7090@gmail.com"


def get_service():
    """
    Authenticate the google api client and return the service object 
    to make further calls
    ARGS
        None
    RETURNS
        service api object from gmail for making calls
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    
    return service



# def get_email(service, msg_id):
#     """
#     Search the inbox for specific message by ID and return it back as a 
#     clean string. String may contain Python escape characters for newline
#     and return line. 
    
#     PARAMS
#         service: the google api service object already instantiated
#         user_id: user id for google api service ('me' works here if
#         already authenticated)
#         msg_id: the unique id of the email you need
#     RETURNS
#         A string of encoded text containing the message body
#     """
#     #try:
#     # grab the message instance
#     message = service.users().messages().get(userId='me', id=msg_id, format='raw').execute()

#     # decode the raw string, ASCII works pretty well here
#     msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

#     # grab the string from the byte object
#     mime_msg = email.message_from_bytes(msg_str)

#     # check if the content is multipart (it usually is)
#     content_type = mime_msg.get_content_maintype()
#     if content_type == 'multipart':
#         # there will usually be 2 parts the first will be the body in text
#         # the second will be the text in html
#         parts = mime_msg.get_payload()

#         # return the encoded text
#         final_content = parts[0].get_payload()
#         return final_content

#     elif content_type == 'text':
#         return mime_msg.get_payload()

#     else:
#         return ""
#         print("\nMessage is not text or multipart, returned an empty string")
#     # except Exception:
#     #   print("An error occured: %s")


# def display_emails(service, msg_ids):
#     """_summary_

#     Args:
#         service: service: the google api service object already instantiated
#         msg_ids: message id
#     """
#     message_choice = input("Would you like to see the emails? (y/n) ").lower()

#     msg_num = 0
#     while (message_choice == 'yes' or message_choice == 'y'):
        
#         message = service.users().messages().get(userId='me', id=msg_ids[msg_num]).execute()
#         email_data = message['payload']['headers']
#         for values in email_data:
#             name = values['name']
#             if name == "From":
#                 from_name = values['value']
#                 print("From: " + from_name)
#                 print("   " + message['snippet'][:50] + "...")
#                 print("\n")

#         msg_num += 1
#         if msg_num == len(msg_ids):
#             message_choice = 'n'
#             print("No more emails, goodbye.")
#         else:
#             message_choice = input("Would you like to see the next email? (y/n) ").lower()



def search_email(service, keyword):
    """
    Search the inbox for emails using standard gmail search parameters
    and return a list of email IDs for each result
    PARAMS:
        service: the google api service object already instantiated
        user_id: user id for google api service ('me' works here if
        already authenticated)
        search_string: search operators you can use with Gmail
        (see https://support.google.com/mail/answer/7190?hl=en for a list)
    RETURNS:
        List containing email IDs of search query
    """
    try:
        # initiate the list for returning
        list_ids = []
        # get the id of all messages that are in the search string
        search_ids = service.users().messages().list(userId='me', q=keyword).execute()
        
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
        
    except Exception:
        print("An error in search_email occured: %s")


def send_email(service, receiver, subject, body):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id
    """

    try:
        message = email.message.EmailMessage()

        message.set_content(body)

        message['To'] = receiver
        #message['From'] = 'testa7090@gmail.com'
        message['Subject'] = subject

        # encoded message
        encoded_message = {
            'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
        }
        
        send_email = (service.users().messages().send(userId="me", body=encoded_message).execute())
        print(F'Message Id: {send_email["id"]}')

    except HttpError as error:
        print(F'An error in send_email occurred: {error}')
        send_email = None

    return send_email



if __name__ == '__main__':

    service = get_service()

    if mode:
        if action == "email":
            service.send_email(recipient, subject, body)
        elif action == "search":
            emails_matched = search_email(service, keyword)
            print("Number of emails with keyword '" + str(keyword) + ": " + str(len(emails_matched)))
            
            if emails_matched:
                print("Email IDs: ", emails_matched)
                #final_content = display_emails(service, emails_matched)
            
        else:
            print("No action selected")

    else:

        # Send email
        #send_email(service, "testa7090@gmail.com", "Test subject", body="This is the test body of the email")

        # Search email for keyword
        keyword='galaxy'
        emails_matched = search_email(service, keyword)
        print("Number of emails with keyword '" + str(keyword) + "': " + str(len(emails_matched)))
        if emails_matched:
            print("Email IDs: ", emails_matched)
            #final_content = display_emails(service, emails_matched)
 