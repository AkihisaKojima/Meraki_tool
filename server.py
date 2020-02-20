from flask import Flask, request, render_template
import pprint

from Lib import getSettings


app = Flask(__name__)

KEY_PATH = "keys/Meraki_API.txt"
with open(KEY_PATH) as f:
	api_key = f.read()


@app.route('/', methods=['GET'])
def root():
	return render_template('main.html', HELLO='Good!')


if __name__ == '__main__':
	app.run(host="0.0.0.0" ,ssl_context=('openssl/server.crt', 'openssl/server.key'), debug=True)
#	app.run(host="0.0.0.0" ,debug=True)
