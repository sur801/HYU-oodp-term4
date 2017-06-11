from flask import render_template
from flask import Flask, request

#from sql_connect import getPerson, getCall, getMsg
import sqlite3
from sql_conn3 import getConnection, getPerson, getCall, getMsg

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

@app.route('/addPerson')
def addPerson():
	return render_template('addPerson.html')

@app.route('/add_entry', methods = ['POST', 'GET'])
def add_entry():
	if request.method == 'POST':
		try:
			name = request.form['name']
			number = request.form['number']
			email = request.form['email']
			
			with getConnection() as conn: 
				curs = conn.cursor()
				curs.execute("INSERT INTO ADDRESSBOOK VALUES(?, ?, ?, ?)", (None, name, number, email))

				conn.commit()

		except:
			conn.rollback()

		finally:
			return render_template('main.html')
			conn.close()


app.run(debug=True, host='0.0.0.0')