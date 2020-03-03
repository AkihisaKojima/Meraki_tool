from flask import Flask, request, render_template, redirect, url_for, make_response
import os

from Lib import Utils


app = Flask(__name__, static_folder='html/static', template_folder='html/templates')

KEY_PATH = 'keys/Meraki_API.txt'
with open(KEY_PATH) as f:
	api_key = f.read()


@app.route('/', methods=['GET'])
def root():
	global api_key

	OrgNet_list = Utils.mk_OrgNetwork_list(api_key)
	html = render_template('main.html', OrgNet_list=OrgNet_list)

	response = make_response(html)
	response.set_cookie('org_id', value = '')
	response.set_cookie('net_id', value = '')
	return response


@app.route('/org', methods=['POST'])
def org():
	try:
		org_name = request.form["org_name"]
		org_id = request.form["org_id"]
	except Exception as e:
		return redirect(url_for('root')) 

	OrgNet_list = Utils.mk_OrgNetwork_list(api_key)
	html = render_template('main.html', OrgNet_list=OrgNet_list)

	response = make_response(html)
	response.set_cookie('org_id', value=org_id)
	return response


@app.route('/net', methods=['POST'])
def net():
	try:
		org_id = request.form["org_id"]
		net_id = request.form["net_id"]
		net_name = request.form["net_name"]
	except Exception as e:
		return redirect(url_for('root')) 

	html = render_template('net.html', Network_name=net_name)

	response = make_response(html)
	response.set_cookie('org_id', value=org_id)
	response.set_cookie('net_id', value=net_id)
	return response


@app.route('/net/<file_name>', methods=['GET'])
def net_general(file_name):
	global api_key

	try:
		net_id = request.cookies.get('net_id')
		org_id = request.cookies.get('org_id')
	except Exception as e:
		return redirect(url_for('root')) 

	if file_name == 'general':
		param = Utils.mk_NetGeneral_param(api_key, net_id)
		return render_template('net_general.html',
			Network_id=net_id, Network_name=param['net_name'], TZ_list=param['TZ_list'], syslog_list=param['syslog_list'])
#		return render_template('net_general.html', Network_id=net_id, Network_name=net_id, TZ_list=net_id)

	elif file_name == 'admin':
		param = Utils.mk_NetAdmin_param(api_key, org_id, net_id)
		return render_template('net_admin.html',
			Network_id=net_id, admin_list=param['admin_list'])
	else:
		return render_template('blank.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True,
			ssl_context=('openssl/server.crt', 'openssl/server.key') )
#	app.run(host="0.0.0.0" ,debug=True)
