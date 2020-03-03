import json
import re

from Lib import getSettings

def mk_OrgNetwork_list(apikey):
	OrgNetwork_list = ''

	orgs = getSettings.get_orgs(apikey)
	list_networks = []
	i = 0
	for org in orgs:
		if org['name'] == 'Gigaraku Promotion':
			continue

		nets = getSettings.get_nets(apikey, org['id'])

		i += 1
		if len(nets) == 0:
			OrgNetwork_list = (OrgNetwork_list +'			<tr><td>\n'
								'				<form method="post" name="form'+str(i)+'" action="/org">\n'
								'				<input type="hidden" name="org_id" value="'+org['id']+'">\n'
								'				<input type="hidden" name="org_name" value="'+org['name']+'">\n'
								'				<a href="javascript:form'+str(i)+'.submit()">'+org['name']+'</a>\n'
								'				</form>\n'
								'				</td>\n')

			Network_list = ('				<td>なし</td>\n'
							'				</tr>\n')

		else:
			OrgNetwork_list = (OrgNetwork_list +'			<tr><td rowspan="'+str(len(nets))+'" valign="top">\n'
								'				<form method="post" name="form'+str(i)+'" action="/org">\n'
								'				<input type="hidden" name="org_id" value="'+org['id']+'">\n'
								'				<input type="hidden" name="org_name" value="'+org['name']+'">\n'
								'				<a href="javascript:form'+str(i)+'.submit()">'+org['name']+'</a>\n'
								'				</form>\n'
								'				</td>\n')

			Network_list = '<<Markup_for_replace>>'
			for net in nets:
				i += 1
				Network_list = (Network_list +'			<tr><td>\n'
								'				<form method="post" name="form'+str(i)+'" action="/net">\n'
								'				<input type="hidden" name="org_id" value="'+org['id']+'">\n'
								'				<input type="hidden" name="net_id" value="'+net['id']+'">\n'
								'				<input type="hidden" name="net_name" value="'+net['name']+'">\n'
								'				<a href="javascript:form'+str(i)+'.submit()">'+net['name']+'</a>\n'
								'				</form>\n'
								'				</td></tr>\n')

			Network_list = Network_list.replace('<<Markup_for_replace>>			<tr><td>\n','			<td>\n')

		OrgNetwork_list = OrgNetwork_list + Network_list

	return OrgNetwork_list


def mk_NetGeneral_param(apikey, net_id):
	mk_NetGeneral_param = {}

	net = getSettings.get_net(apikey, net_id)

	mk_NetGeneral_param['net_name'] = net['name']

	f_path = 'data/TimeZone_list.txt'
	with open(f_path) as f:
		TZ_list = f.read()
	mk_NetGeneral_param['TZ_list'] = TZ_list.replace(net['timeZone'], net['timeZone'] +'" selected="selected"')

	syslogs = getSettings.get_syslogs(apikey, net_id)
	syslog_list = ''
	i = 1
	for syslog in syslogs:
		checked_flows = ''
		checked_urls = ''
		checked_appliance = ''
		checked_airMarshal = ''
		checked_wireless = ''
		checked_switch = ''
		for role in syslog['roles']:
			if str.lower(role) == 'flows':
				checked_flows = ' checked="checked"'
			elif str.lower(role) == 'urls':
				checked_urls = ' checked="checked"'
			elif str.lower(role) == 'appliance event log':
				checked_appliance = ' checked="checked"'
			elif str.lower(role) == 'air marshal events':
				checked_airMarshal = ' checked="checked"'
			elif str.lower(role) == 'wireless event log':
				checked_wireless = ' checked="checked"'
			elif str.lower(role) == 'switch event log':
				cchecked_switch = ' checked="checked"'
		syslog_list = (syslog_list + 
			'						<div><div class="value"><input type="text" name="net_syslog_ip_'+ str(i) +'" size="17" maxlength="15" value="'+ syslog['host'] +'"></div>\n'
			'							<div class="value"><input type="text" name="net_syslog_port_'+ str(i) +'" size="10" maxlength="5" value="'+ str(syslog['port']) +'"></div>\n'
			'							<div class="value"><input type="checkbox" name="net_syslog_flows_'+ str(i) +'" value="1"'+ checked_flows +'>Flows\n'
			'								<input type="checkbox" name="net_syslog_urls_'+ str(i) +'" value="1"'+ checked_urls +'>URLs\n'
			'								<input type="checkbox" name="net_syslog_appliance_'+ str(i) +'" value="1"'+ checked_appliance +'>Appliance event log\n'
			'								<input type="checkbox" name="net_syslog_airMarshal_'+ str(i) +'" value="1"'+ checked_airMarshal +'>Air Marshal events\n'
			'								<input type="checkbox" name="net_syslog_wireless_'+ str(i) +'" value="1"'+ checked_wireless +'>Wireless event log\n'
			'								<input type="checkbox" name="net_syslog_switch_'+ str(i) +'" value="1"'+ cchecked_switch +'>Switch event log\n'
			'								</div>\n'
			'							<div class="value"><input id="del_btn_'+ str(i) +'" type="button" value="削除" onclick="del_btn(this)"/></div></div>\n')

		i += 1

	mk_NetGeneral_param['syslog_list'] = syslog_list

	return mk_NetGeneral_param


def mk_NetAdmin_param(apikey, org_id, net_id):
	mk_NetAdmin_param = {}

	admins = getSettings.get_admins(apikey, org_id)

	admin_list = '\n'
	i = 0
	for admin in admins:
		for net in admin['networks']:
			if net['id'] == net_id:
				if net['access'] == 'full':
					select_option = '<option value="full" selected>full</option><option value="read-only">read-only</option><option value="enterprise">enterprise</option><option value="none">none</option>'
				elif net['access'] == 'read-only':
					select_option = '<option value="full">full</option><option value="read-only" selected>read-only</option><option value="enterprise">enterprise</option><option value="none">none</option>'
				elif net['access'] == 'enterprise':
					select_option = '<option value="full">full</option><option value="read-only">read-only</option><option value="enterprise" selected>enterprise</option><option value="none">none</option>'
				elif net['access'] == 'none':
					select_option = '<option value="full">full</option><option value="read-only">read-only</option><option value="enterprise">enterprise</option><option value="none" selected>none</option>'

				admin_list = (admin_list + 
					'						<tr><td><input type="text" name="net_username_'+ str(i) +'" value="'+ admin['name'] +'"></td>\n'
					'							<td><input type="text" name="net_mail_'+ str(i) +'" value="'+ admin['email'] +'"></td>\n'
					'							<td><input type="text" name="net_status_'+ str(i) +'" value="'+ admin['accountStatus'] +'"></td>\n'
					'							<td><select name="net_access_'+ str(i) +'">'+ select_option +'</select></td>\n'
					'							<td><input id="del_btn_'+ str(i) +'" type="button" value="削除" onclick="del_btn(this)"/></td></tr>\n')
				i += 1

	mk_NetAdmin_param['admin_list'] = admin_list

	return mk_NetAdmin_param
