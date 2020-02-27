import requests, json

BASEURL = 'https://api.meraki.com/api/v0/'

def get_org(apikey):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'organizations'
	orgs = requests.get(url, headers=headers).json()

	return orgs


def get_net(apikey, org_id):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'organizations/' + org_id + '/networks'
	nets = requests.get(url, headers=headers).json()

	return nets
