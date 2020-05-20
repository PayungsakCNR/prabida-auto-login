## PSU Pra-bi-da Internet Auto Login.

- This project require os,request,subprocess,time,datetime package.


### How to run
1. Clone this project and make sure python3 and pip3 already installed.
2. Install require package by $sudo pip3 install -r requirements.txt.
3. Modify .env file to your PSU Passport credential.
4. Run this script by $python3 prabida-auto-login.py
5. Use crontab for auto login.

### Tip
- Set alertToLine = False for not aleart to Line Notify.
- Set alertToLine = True for aleart to Line Notify.
- If  alertToLine = True , please add LINE_NOTIFY_TOKEN=xxxx in .env file.


