import requests, json

BASEURL = 'https://api.meraki.com/api/v0/'

def get_orgs(apikey):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'organizations'
	orgs = requests.get(url, headers=headers).json()

	return orgs


def get_nets(apikey, org_id):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'organizations/' + org_id + '/networks'
	nets = requests.get(url, headers=headers).json()

	return nets


def get_net(apikey, net_id):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'networks/' + net_id
	net = requests.get(url, headers=headers).json()

	return net


def get_admins(apikey, org_id):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + '/organizations/' + org_id + '/admins'
	admins = requests.get(url, headers=headers).json()

	return admins


def get_syslogs(apikey, net_id):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'networks/' + net_id + '/syslogServers'
	syslogs = requests.get(url, headers=headers).json()

	return syslogs


def get_alert(apikey, net_id):
	headers = { 'X-Cisco-Meraki-API-Key': apikey,
				'Content-Type': 'application/json' }
	url = BASEURL + 'networks/' + net_id + '/networks/' + net_id + '/alertSettings'
	alert = requests.get(url, headers=headers).json()

	return alert
