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
			'						<div class="table_tr">\n'
			'							<div class="value border_bottom"><input type="text" name="net_syslog_ip_'+ str(i) +'" size="17" maxlength="15" value="'+ syslog['host'] +'"></div>\n'
			'							<div class="value border_bottom"><input type="text" name="net_syslog_port_'+ str(i) +'" size="10" maxlength="5" value="'+ str(syslog['port']) +'"></div>\n'
			'							<div class="value border_bottom"><input type="checkbox" name="net_syslog_flows_'+ str(i) +'" value="1"'+ checked_flows +'>Flows\n'
			'								<input type="checkbox" name="net_syslog_urls_'+ str(i) +'" value="1"'+ checked_urls +'>URLs\n'
			'								<input type="checkbox" name="net_syslog_appliance_'+ str(i) +'" value="1"'+ checked_appliance +'>Appliance event log\n'
			'								<input type="checkbox" name="net_syslog_airMarshal_'+ str(i) +'" value="1"'+ checked_airMarshal +'>Air Marshal events\n'
			'								<input type="checkbox" name="net_syslog_wireless_'+ str(i) +'" value="1"'+ checked_wireless +'>Wireless event log\n'
			'								<input type="checkbox" name="net_syslog_switch_'+ str(i) +'" value="1"'+ cchecked_switch +'>Switch event log\n'
			'								</div>\n'
			'							<div class="value border_bottom"><input id="del_btn_'+ str(i) +'" type="button" value="削除" onclick="del_btn(this)"/></div>\n'
			'						</div>\n')

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
					'						<div class="table_tr">\n'
					'							<div class="value"><input type="text" name="net_username_'+ str(i) +'" value="'+ admin['name'] +'"></div>\n'
					'							<div class="value"><input type="text" name="net_mail_'+ str(i) +'" value="'+ admin['email'] +'"></div>\n'
					'							<div class="value"><input type="text" name="net_status_'+ str(i) +'" value="'+ admin['accountStatus'] +'"></div>\n'
					'							<div class="value"><select name="net_access_'+ str(i) +'">'+ select_option +'</select></div>\n'
					'							<div class="value"><input id="del_btn_'+ str(i) +'" type="button" value="削除" onclick="del_btn(this)"/></div>\n'
					'						</div>\n')
				i += 1

	mk_NetAdmin_param['admin_list'] = admin_list

	return mk_NetAdmin_param


def mk_NetAlert_param(apikey, net_id):
	mk_NetAlert_param = {}
	mk_NetAlert_param['net_alert_admin_name'] = ''
	mk_NetAlert_param['net_alert_ch_setting'] = ''
	mk_NetAlert_param['net_alert_ch_vpnconnect'] = ''
	mk_NetAlert_param['net_alert_dt_marAP'] = ''
	mk_NetAlert_param['net_alert_dt_trafficover'] = ''
	mk_NetAlert_param['th_traffic'] = ''
	mk_NetAlert_param['th_traffic_unit_k'] = ''
	mk_NetAlert_param['th_traffic_unit_m'] = ''
	mk_NetAlert_param['th_traffic_unit_g'] = ''
	mk_NetAlert_param['th_traffic_unit_t'] = ''
	mk_NetAlert_param['th_period_20m'] = ''
	mk_NetAlert_param['th_period_4h'] = ''
	mk_NetAlert_param['th_period_1d'] = ''
	mk_NetAlert_param['net_alert_dt_apdown'] = ''
	mk_NetAlert_param['th_apduwn_5'] = ''
	mk_NetAlert_param['th_apduwn_10'] = ''
	mk_NetAlert_param['th_apduwn_15'] = ''
	mk_NetAlert_param['th_apduwn_30'] = ''
	mk_NetAlert_param['th_apduwn_60'] = ''
	mk_NetAlert_param['net_alert_dt_repeaterdown'] = ''
	mk_NetAlert_param['th_repeaterduwn_5'] = ''
	mk_NetAlert_param['th_repeaterduwn_10'] = ''
	mk_NetAlert_param['th_repeaterduwn_15'] = ''
	mk_NetAlert_param['th_repeaterduwn_30'] = ''
	mk_NetAlert_param['th_repeaterduwn_60'] = ''
	mk_NetAlert_param['net_alert_ch_gateway'] = ''
	mk_NetAlert_param['net_alert_dt_mxdown'] = ''
	mk_NetAlert_param['net_alert_ch_uplink'] = ''
	mk_NetAlert_param['net_alert_dt_dhcperr'] = ''
	mk_NetAlert_param['net_alert_dt_ipcollision'] = ''
	mk_NetAlert_param['net_alert_dt_mardhcp'] = ''
	mk_NetAlert_param['net_alert_dt_failover'] = ''
	mk_NetAlert_param['net_alert_dt_client'] = ''
	mk_NetAlert_param['dt_client'] = ''
	mk_NetAlert_param['net_alert_dt_msdown'] = ''
	mk_NetAlert_param['th_msdown_5'] = ''
	mk_NetAlert_param['th_msdown_10'] = ''
	mk_NetAlert_param['th_msdown_15'] = ''
	mk_NetAlert_param['th_msdown_30'] = ''
	mk_NetAlert_param['th_msdown_60'] = ''
	mk_NetAlert_param['net_alert_dt_dhcp'] = ''
	mk_NetAlert_param['net_alert_dt_portdown'] = ''
	mk_NetAlert_param['th_portdown_5'] = ''
	mk_NetAlert_param['th_portdown_10'] = ''
	mk_NetAlert_param['th_portdown_15'] = ''
	mk_NetAlert_param['th_portdown_30'] = ''
	mk_NetAlert_param['th_portdown_60'] = ''
	mk_NetAlert_param['net_alert_dt_cableerr'] = ''
	mk_NetAlert_param['net_alert_ch_linkspeed'] = ''
	mk_NetAlert_param['net_alert_dt_nopower'] = ''
	mk_NetAlert_param['net_alert_dt_redundantpower'] = ''
	mk_NetAlert_param['net_alert_dt_udld'] = ''
	mk_NetAlert_param['net_alert_dt_hightemp'] = ''
	mk_NetAlert_param['webhook_list'] = ''

	alert = getSettings.get_alert(apikey, net_id)


	return mk_NetAlert_param


def render_template_alert(template, param):
	net_alert_admin_name = param['net_alert_admin_name']
	net_alert_ch_setting = param['net_alert_ch_setting']
	net_alert_ch_vpnconnect = param['net_alert_ch_vpnconnect']
	net_alert_dt_marAP = param['net_alert_dt_marAP']
	net_alert_dt_trafficover = param['net_alert_dt_trafficover']
	th_traffic = param['th_traffic']
	th_traffic_unit_k = param['th_traffic_unit_k']
	th_traffic_unit_m = param['th_traffic_unit_m']
	th_traffic_unit_g = param['th_traffic_unit_g']
	th_traffic_unit_t = param['th_traffic_unit_t']
	th_period_20m = param['th_period_20m']
	th_period_4h = param['th_period_4h']
	th_period_1d = param['th_period_1d']
	net_alert_dt_apdown = param['net_alert_dt_apdown']
	th_apduwn_5 = param['th_apduwn_5']
	th_apduwn_10 = param['th_apduwn_10']
	th_apduwn_15 = param['th_apduwn_15']
	th_apduwn_30 = param['th_apduwn_30']
	th_apduwn_60 = param['th_apduwn_60']
	net_alert_dt_repeaterdown = param['net_alert_dt_repeaterdown']
	th_repeaterduwn_5 = param['th_repeaterduwn_5']
	th_repeaterduwn_10 = param['th_repeaterduwn_10']
	th_repeaterduwn_15 = param['th_repeaterduwn_15']
	th_repeaterduwn_30 = param['th_repeaterduwn_30']
	th_repeaterduwn_60 = param['th_repeaterduwn_60']
	net_alert_ch_gateway = param['net_alert_ch_gateway']
	net_alert_dt_mxdown = param['net_alert_dt_mxdown']
	net_alert_ch_uplink = param['net_alert_ch_uplink']
	net_alert_dt_dhcperr = param['net_alert_dt_dhcperr']
	net_alert_dt_ipcollision = param['net_alert_dt_ipcollision']
	net_alert_dt_mardhcp = param['net_alert_dt_mardhcp']
	net_alert_dt_failover = param['net_alert_dt_failover']
	net_alert_dt_client = param['net_alert_dt_client']
	dt_client = param['dt_client']
	net_alert_dt_msdown = param['net_alert_dt_msdown']
	th_msdown_5 = param['th_msdown_5']
	th_msdown_10 = param['th_msdown_10']
	th_msdown_15 = param['th_msdown_15']
	th_msdown_30 = param['th_msdown_30']
	th_msdown_60 = param['th_msdown_60']
	net_alert_dt_dhcp = param['net_alert_dt_dhcp']
	net_alert_dt_portdown = param['net_alert_dt_portdown']
	th_portdown_5 = param['th_portdown_5']
	th_portdown_10 = param['th_portdown_10']
	th_portdown_15 = param['th_portdown_15']
	th_portdown_30 = param['th_portdown_30']
	th_portdown_60 = param['th_portdown_60']
	net_alert_dt_cableerr = param['net_alert_dt_cableerr']
	net_alert_ch_linkspeed = param['net_alert_ch_linkspeed']
	net_alert_dt_nopower = param['net_alert_dt_nopower']
	net_alert_dt_redundantpower = param['net_alert_dt_redundantpower']
	net_alert_dt_udld = param['net_alert_dt_udld']
	net_alert_dt_hightemp = param['net_alert_dt_hightemp']
	webhook_list = param['webhook_list']

return render_template(template,
		net_alert_admin_name=net_alert_admin_name,
		net_alert_ch_setting=net_alert_ch_setting,
		net_alert_ch_vpnconnect=net_alert_ch_vpnconnect,
		net_alert_dt_marAP=net_alert_dt_marAP,
		net_alert_dt_trafficover=net_alert_dt_trafficover,
		th_traffic=th_traffic,
		th_traffic_unit_k=th_traffic_unit_k,
		th_traffic_unit_m=th_traffic_unit_m,
		th_traffic_unit_g=th_traffic_unit_g,
		th_traffic_unit_t=th_traffic_unit_t,
		th_period_20m=th_period_20m,
		th_period_4h=th_period_4h,
		th_period_1d=th_period_1d,
		net_alert_dt_apdown=net_alert_dt_apdown,
		th_apduwn_5=th_apduwn_5,
		th_apduwn_10=th_apduwn_10,
		th_apduwn_15=th_apduwn_15,
		th_apduwn_30=th_apduwn_30,
		th_apduwn_60=th_apduwn_60,
		net_alert_dt_repeaterdown=net_alert_dt_repeaterdown,
		th_repeaterduwn_5=th_repeaterduwn_5,
		th_repeaterduwn_10=th_repeaterduwn_10,
		th_repeaterduwn_15=th_repeaterduwn_15,
		th_repeaterduwn_30=th_repeaterduwn_30,
		th_repeaterduwn_60=th_repeaterduwn_60,
		net_alert_ch_gateway=net_alert_ch_gateway,
		net_alert_dt_mxdown=net_alert_dt_mxdown,
		net_alert_ch_uplink=net_alert_ch_uplink,
		net_alert_dt_dhcperr=net_alert_dt_dhcperr,
		net_alert_dt_ipcollision=net_alert_dt_ipcollision,
		net_alert_dt_mardhcp=net_alert_dt_mardhcp,
		net_alert_dt_failover=net_alert_dt_failover,
		net_alert_dt_client=net_alert_dt_client,
		dt_client=dt_client,
		net_alert_dt_msdown=net_alert_dt_msdown,
		th_msdown_5=th_msdown_5,
		th_msdown_10=th_msdown_10,
		th_msdown_15=th_msdown_15,
		th_msdown_30=th_msdown_30,
		th_msdown_60=th_msdown_60,
		net_alert_dt_dhcp=net_alert_dt_dhcp,
		net_alert_dt_portdown=net_alert_dt_portdown,
		th_portdown_5=th_portdown_5,
		th_portdown_10=th_portdown_10,
		th_portdown_15=th_portdown_15,
		th_portdown_30=th_portdown_30,
		th_portdown_60=th_portdown_60,
		net_alert_dt_cableerr=net_alert_dt_cableerr,
		net_alert_ch_linkspeed=net_alert_ch_linkspeed,
		net_alert_dt_nopower=net_alert_dt_nopower,
		net_alert_dt_redundantpower=net_alert_dt_redundantpower,
		net_alert_dt_udld=net_alert_dt_udld,
		net_alert_dt_hightemp=net_alert_dt_hightemp,
		webhook_list=webhook_list)
