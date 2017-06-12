from flask import render_template
from flask import Flask, request, flash, redirect, url_for

#from sql_connect import getPerson, getCall, getMsg
import sqlite3
from sql_conn3 import getConnection, getPerson, getCall, getMsg, setPerson, searchPerson, searchName, changePerson, deletePerson, searchById , addCall, addSms

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods = ['POST','GET'])
def main(name=None):
	if(request.method == 'POST'):
		key = request.form['keyword']
		return render_template('main.html', person=searchPerson(key))
		#return render_template('searchResult.html',s_person=searchPerson(key))
	
	return render_template('main.html', name=name, person=getPerson())


@app.route('/call_hist')
def call_hist():
	return render_template('call_hist.html', call=getCall())

@app.route('/searchResult')
def searchResult():
	return render_template('searchResult.html')
	
@app.route('/sms_hist/<int:id>', methods = ['GET','POST'])
def sms_hist(id):
	error = None
	if request.method == 'POST':
		text = request.form['content']

		if not text:
			error = 'Blank not allowed! Please fill in the all fields.'
			return render_template('Messaging.html', error=error)
		else:
			person_sms = searchById(id)
			addSms(person_sms[0][2],text)
			return render_template('sms_hist.html', sms=getMsg())
	else:
		return render_template('sms_hist.html', sms=getMsg())



# @app.route('/delete', methods = ['POST','GET'])
# def delete():
# 	value = request.data
# 	deletePerson(value)
# 	print (value)
# 	return redirect(url_for('editPerson'))


@app.route('/addPerson', methods = ['POST', 'GET'])
def addPerson():
	error = None

	if request.method == 'POST':

		name = request.form['name']
		number = request.form['number']
		email = request.form['email']

		# TODO : Duplicate Check : not ready
		if searchName(number):
			error = 'Number is already in the Addressbook.'

		elif not name or not number or not email:
			error = 'Blank not allowed! Please fill in the all fields.'

		else:
			setPerson(name, number, email)
			return redirect(url_for('main'))

	return render_template('addPerson.html', error=error)

@app.route('/update', methods = ['POST', 'GET'])
def updatePerson():
	error = None

	if request.method == 'POST':

		name = request.form['name']
		number = request.form['number']
		email = request.form['email']
		id = request.form['id']

		# TODO : Duplicate Check : not ready
		if searchName(number):
			error = 'Number is already in the Addressbook.'

		elif not name or not number or not email:
			error = 'Blank not allowed! Please fill in the all fields.'

		else:
			changePerson(name, number, email,id)
			return redirect(url_for('main'))

	return render_template('editPerson.html', error=error)


@app.route('/delete/<int:id>', methods = ['DELETE'])
def deleteUser(id):
	deletePerson(id)
	return redirect(url_for('main', person=getPerson()))
	#return "ok", 200
@app.route('/edit/<int:id>', methods = ['GET'])
def editUser(id):
	#
	print(id)
	return render_template('editPerson.html', person=searchById(id))
	#return redirect(url_for('main'))

@app.route('/make_sms/<int:id>', methods = ['GET','POST'])
def makeSms(id):
	person = searchById(id)
	text = "hello"
	addSms(person[0][2],text)
	return render_template('sms_hist.html', sms=getMsg())
	#return render_template('editPerson.html', person=searchById(id))
	#return redirect(url_for('main'))



@app.route('/Messaging/<int:id>', methods = ['GET','POST'])
def Messaging(id):
	return render_template('Messaging.html', person=searchById(id))


@app.route('/make_call/<int:id>', methods = ['GET'])
def makeCall(id):
	person = searchById(id)
	addCall(person[0][2])
	return render_template('call_hist.html', call=getCall())



app.run(debug=True, host='0.0.0.0')