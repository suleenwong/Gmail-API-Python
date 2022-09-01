## Gmail API connection setup


**Step 1: Create a project**
- Open the [Google Cloud console](https://console.cloud.google.com/)
- Click on **Select a project** and then **New Project**
- Give a project name and create

<br>

**Step 2: Configure the OAuth consent screen:**
<br>
- Click on the top left navigation menu > APIs & Services > OAuth consent screen
- Select the project created in Step 1
- Choose user type External/Internal based on your requirement, in this case we choose **External** and click Create
- On the next screen
    - Give an app name
    - Choose Support email
    - Add logo (optional)
    - At the bottom add Developer email and create
- In next Screen
    - Save and continue
- In next Screen
    - Add a test user with valid email
    - Save and continue

<br>

**Step 3. Creating OAuth ClientId**
- Click on **Credentials** from the left panel
- Hit the **+ CREATE CREDENTIALS** button on top bar.
    - Select **OAuth client ID**
    - Application type **Desktop App**
    - Create
    - Download json, rename it as 'credential.json' and paste it inside project folder
