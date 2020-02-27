import json

from Lib import getSettings

def mk_OrgNetwork_list(apikey):
	OrgNetwork_list = ''

	orgs = getSettings.get_org(apikey)
	list_networks = []
	i = 0
	for org in orgs:
		if org['name'] == 'Gigaraku Promotion':
			continue

		nets = getSettings.get_net(apikey, org['id'])

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
								'				<input type="hidden" name="net_id" value="'+net['id']+'">\n'
								'				<input type="hidden" name="net_name" value="'+net['name']+'">\n'
								'				<a href="javascript:form'+str(i)+'.submit()">'+net['name']+'</a>\n'
								'				</form>\n'
								'				</td></tr>\n')

			Network_list = Network_list.replace('<<Markup_for_replace>>			<tr><td>\n','			<td>\n')

		OrgNetwork_list = OrgNetwork_list + Network_list

	return OrgNetwork_list


def get_net(apikey, org_id):
	url = baseurl + 'organizations/' + org_id + '/networks'
	nets = requests.get(url, headers=headers).json()

	return nets
