from flask import Flask, request, render_template, redirect, url_for
import pprint

from Lib import Utils


app = Flask(__name__, static_folder='html/static', template_folder='html/templates')

KEY_PATH = 'keys/Meraki_API.txt'
api_key = ''
with open(KEY_PATH) as f:
	api_key = f.read()


@app.route('/', methods=['GET'])
def root():
	global api_key

	OrgNet_list = Utils.mk_OrgNetwork_list(api_key)
	return render_template('main.html', OrgNet_list=OrgNet_list)


@app.route('/org', methods=['POST'])
def org():
	try:
		org_name = request.form["org_name"]
	except Exception as e:
		return redirect(url_for('root')) 

	OrgNet_list = Utils.mk_OrgNetwork_list(api_key)
	return render_template('main.html', OrgNet_list=OrgNet_list)


@app.route('/net', methods=['POST'])
def net():
	try:
		net_name = request.form["net_name"]
	except Exception as e:
		return redirect(url_for('root')) 

	return render_template('net.html', Network_name=net_name)


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True,
			ssl_context=('openssl/server.crt', 'openssl/server.key') )
#	app.run(host="0.0.0.0" ,debug=True)
