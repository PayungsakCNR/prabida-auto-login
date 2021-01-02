'''
PSU Pra-bi-da Internet Auto Log in.
Version 1.0.3 | 01/09/2019
Payungsak Klinchampa | CoE-PSU
pao@payungsakpk.xyz
'''

import os
import requests
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

scriptVersion = 'v1.0.3'
PSU_URL = 'https://cp-xml-40g.psu.ac.th:6082/php/uid.php'
alertToLine = False ###Set default config to False.

def sendToLineNotify():
	encoding = 'utf-8'
	cur_time = datetime.now()
	LINE_URL = 'https://notify-api.line.me/api/notify'
	token = os.getenv('LINE_NOTIFY_TOKEN')
	headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}
	
	getHostname = subprocess.check_output("hostname", shell=True)
	
	msg = '\nPSU Prabida Auto Login\n\n' + 'Time: ' + cur_time.strftime('%Y/%m/%d %H:%M:%S') +'\nHostname: ' + getHostname.decode(encoding) + '\nLog in successful !!'
	
	r = requests.post(LINE_URL, headers=headers , data = {'message':msg})
	jsonRes = r.json()
	if r.status_code == 200:
		print('Alert to Line notify OK')
	else:
		print('Can not alert to Line notify')

def checkPing():
	host_ip = '1.1.1.1' #Check ping res by Cloudflare Public DNS server
	try:
		output = subprocess.check_output("ping -c 1 -W 3 {}".format(host_ip), shell=True)
	except Exception as e:
		return False
	return True

def login():
	headers = {'User-Agent': 'PSU Pra-bi-da Auto Login - ' + scriptVersion}
	payload = {
		'username' : os.getenv('PSU_USERNAME'),
		'password' : os.getenv('PSU_PASSWORD'),
		'login': 'Login'
	}
	
	s = requests.Session()
	get_login = s.get(PSU_URL)
	cookies = dict(get_login.cookies)
	#print(get_login.headers)
	
	post_login = s.post(PSU_URL, headers=headers, data=payload, cookies=cookies)
	#print(post_login.text)
	time.sleep(5) ## Sleep 5s.

	if(checkPing() == True):
		print('Log in successful !!')
		if(alertToLine == True):
			sendToLineNotify()
	else:
		print('Error , Please try again')

def main():
	if(checkPing() == False):
		print('NOT LOGIN !!')
		login() # Call login() function
	else:
		print('Already Loged in!!') 


main() ## Main Function
