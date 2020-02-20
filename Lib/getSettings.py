import requests
import pprint
from collections import defaultdict

# user specified variables
apikey = '8f2e0045ccc4a8bb134a3af7c855d65a9a07e2d4'

# static variable
headers = { 'X-Cisco-Meraki-API-Key': apikey, }
#baseurl = "https://dashboard.meraki.com/api/v0/"
baseurl = 'https://api.meraki.com/api/v0/'

# Retrieve organization list which I'm belonging to
url = baseurl + 'organizations'
orgs = requests.get(url, headers=headers).json()
#pprint.pprint(orgs)

for org in orgs:
	print(org['name'])
	print(org['id'])
	
	if 'managed' in org['name'].lower():
		url = baseurl + 'organizations/' + org['id'] + '/devices'
		devices = requests.get(url, headers=headers).json()
		pprint.pprint(devices)
	
	print('')
