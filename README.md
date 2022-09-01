# Python Google API Challenge

This is a repository for an application to utilize the Google API using Python for Gmail operations. The Gmail API documentation by Google is available at https://developers.google.com/gmail/api/

<br>

## Task
- setup a test gmail account and enable the APIs for it
- cover the following features:
    - send emails
    - search for specific messages in the mailbox, e.g. for keywords in subject or body text
- a brief documentation of your steps in terms what is needed to setup this API connection, PLEASE in your words not just copy & paste from google

<br>

# Requirements

- Python (2.6 or higher)
- A Google account with Gmail enabled
- Google API client and Google OAuth libraries

<br>


# Setup

**Step 1: Clone this repository**
```zsh
git clone git@github.com:suleenwong/Gmail-API-Python.git
```

<br>

**Step 2: Install the Google client library**
```zsh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

<br>

**Step 3: Setup and configure the Gmail API connection**

For a new Gmail account, the instructions setup and configure a Gmail API connection can be found here: [Gmail API setup](GmailAPIsetup.md)

<br>

**Step 4: Authenticate**

Before running the program initial setup is necessary. Make sure a working credentials.json file from the [Gmail API setup](GmailAPIsetup.md) is in the project folder. 

Next, from the command line, execute the following command:
<br>
```zsh
python gmail_helper.py
```

Enter the account you added as test user and press Continue twice.

Once it is enabled you will see "The authentication flow has completed. You may close this window." as confirmation.

<br>

# Usage


### To display help:
```zsh
python gmail_helper.py --help
```

### To send an email:
```zsh
python gmail_helper.py --action send -e "testa7090@gmail.com" -s "galaxy" -b "hello universe"
```

### To search emails with a keyword:
```zsh
python gmail_helper.py --action search -k "hello world" 
```