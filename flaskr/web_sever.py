from flask import render_template
from flask import Flask

from sql_connect import getPerson

app = Flask(__name__)

@app.route('/')
def main(name=None):
    return render_template('main.html', name=name, person=getPerson())

@app.route('/call_hist')
def call_hist():
	return render_template('call_hist.html')
	
app.run(debug=True)