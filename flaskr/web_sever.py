from flask import render_template
from flask import Flask

from sql_connect import getPerson, getCall, getMsg

app = Flask(__name__)

@app.route('/')
def main(name=None):
    return render_template('main.html', name=name, person=getPerson())

@app.route('/call_hist')
def call_hist():
	return render_template('call_hist.html', call=getCall())
	
@app.route('/sms_hist')
def sms_hist():
	return render_template('sms_hist.html', sms=getMsg())

app.run(debug=True, host='0.0.0.0')