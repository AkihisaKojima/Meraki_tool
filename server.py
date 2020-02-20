from flask import Flask, request, render_template
import pprint


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def root():
	return render_template('main.html', HELLO='hello')


if __name__ == '__main__':
#	app.run(host="0.0.0.0" ,ssl_context=('openssl/server.crt', 'openssl/server.key'), debug=True)
	app.run(host="0.0.0.0" ,debug=True)
