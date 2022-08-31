# Python Google API Challenge

This is a repository for an application to utilize the Google API using Python for Gmail operations. The Gmail API documentation by Google is available at https://developers.google.com/gmail/api/

## Task
- setup a test gmail account and enable the APIs for it
- cover the following features:
    - send emails
    - search for specific messages in the mailbox, e.g. for keywords in subject or body text
- a brief documentation of your steps in terms what is needed to setup this API connection, PLEASE in your words not just copy & paste from google

## Functionality of this Python script
- send email
- read emails
- search for emails with specific keywords

## Requirements

- Python 3.9.8
- pip
- Gmail account with ... enabled

<br>

## Gmail API connection setup

<br>

**Step 1: Clone this repository**
```zsh
git clone 
```

<br>

**Step 2: Install the Google client library**
```zsh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

<br>

**Step 3: Create a project**
- Open the [Google Cloud console](https://console.cloud.google.com/)
- Click on **Select a project** and then **New Project**
- Give a project name and create


<br>

<!-- 1. Create a gmail account 
Go to https://console.cloud.google.com/getting-started, click on "Select a project" and then "New Project"

3. Enable API
- make sure your project is selected
- go to navigation bar on the top left > APIs & Services > Library
- Search for "Gmail API", click on it, then click on "Enable" -->

**Step 4: Configure the OAuth consent screen:**
<br>
- Open the [Google Cloud console](https://console.cloud.google.com/)
- Click on the top left navigation menu > APIs & Services > OAuth consent screen
- Select project created in Step 3
- Choose user type External/Internal based on your requirement, in this case we choose External and click Create
- On the next screen
    - Give an app name
    - Choose Support email
    - Add logo if you have any
    - At the bottom add Developer email and create
- In next Screen
    - Save and continue
- In next Screen
    - Add a test user with valid email id
    - Save and continue

<br>

**Step 5. Creating OAuth ClientId**
- Click on **Credentials** from the left panel
- Hit the **+ CREATE CREDENTIALS** button on top bar.
    - Select **OAuth client ID**
    - Application type **Desktop App**
    - Create
    - Download json and rename it as credential.json and paste it inside project folder

<!-- go to navigation bar on top left > APIs & Services > OAuth Consent Screen
create OAuth Consent Screen > External
- Enter app name, user support email and developer contact information
add https://mail.google.com/ scope and update
add test user
check test user and scopes in summary section -->



## Usage

run get_email.py


"The authentication flow has completed. You may close this window."

Make sure credentials.json file is in the project folder

Once it is enabled you will see "The authentication flow has completed. You may close this window." IN that window as confirmation.



## Usage

Before Running the program Initial setup is necessary. Make sure you have both working credentials.json and token.json both inside the project folder.


1. From the command line, execute the following command:
<br>
```zsh
python gmail_api_helper.py
```

2. get_email.py

3. send email: send_message()
<br>
search: search_message()


