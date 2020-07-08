from flask import render_template, redirect, url_for, request
from flask_sqlalchemy import SQLalchemy
import requests

app = Flask(__name__)
db = SQLalchemy(app)

app.config['SQLALCHEMY_DATABASE_URI']
app.config['SECRET_KEY']

class tickets(db.Model):
	id = db.Column(db.Integer, primarykey=True)
	letterstring = db.Column(db.String(7))
	primeno = db.Column(db.Integer)
	win = db.Column(db.Boolean)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home:')

@app.route('/home/generate')
def generate():
	all_tickets=tickets.query.all()
	letterstring = requests.get('http://app2:5001/letterstring')
	primeno = requests.get('http://app3:5002/primeno')
	checkstring = requests.post('http://app4:5003/checkstring', data=letterstring)
	checkprime = requests.post('http://app4:5003/checkprime', data=primeno)
	if (checkstring == 'True' & checkprime=='True'):
		win=True
		ticket = tickets(
			letterstring=letterstring,
			primeno=primeno,
			win=win
		)
		db.session.add(ticket)
		db.session.commit()
	else:
		win=False
	return render_template('home.html', title='Home:',tickets=all_tickets)


if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
