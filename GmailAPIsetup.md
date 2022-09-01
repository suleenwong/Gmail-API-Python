## Gmail API connection setup

For a new Gmail account, the following steps should be done to setup the Gmail API connection:

**Step 1: Create a project**
- Open the [Google Cloud console](https://console.cloud.google.com/)
- Click on **Select a project** and then **New Project**
- Give a project name and create
- Select the project that was just created

<br>

**Step 2: Configure the OAuth consent screen:**
<br>
- Click on the top left navigation menu > APIs & Services > OAuth consent screen
- Select the project created in Step 1
- Choose user type External/Internal based on your requirement, in this case we choose **External** and click Create
- On the **OAuth consent screen**
    - Give an app name
    - Choose Support email
    - At the bottom add Developer email
    - Save and continue
- On the next screen
    - Save and continue
- On the next screen
    - **+ Add users**
    - Add the email of the Gmail account that was just created 
    - Save and continue

<br>

**Step 3. Creating OAuth ClientId**
- Click on **Credentials** from the left panel
- Hit the **+ CREATE CREDENTIALS** button on top bar.
    - Select **OAuth client ID**
    - Application type **Desktop App**
    - Create
    - Download json, rename it as 'credential.json' and paste it inside project folder
