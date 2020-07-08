from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

class tickets(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	letterstring = db.Column(db.String(7))
	primeno = db.Column(db.Integer)
	win = db.Column(db.Boolean)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home:')

@app.route('/home/generate')
def home_generate():
	all_tickets=tickets.query.all()
	letterstring = requests.get('http://app2:5001/letterstring')
	primeno = requests.get('http://app3:5002/primeno')
	checkstring = requests.post('http://app4:5003/checkstring', data=letterstring.text)
	checkprime = requests.post('http://app4:5003/checkprime', data=primeno.text)
	if checkstring.text == 'True' and checkprime.text == 'True':
		win=True
	else:
		win=False
	ticket = tickets(
			letterstring=intletterstring.text,
			primeno=int(primeno.text),
			win=win
		)
	db.session.add(ticket)
	db.session.commit()
	return render_template('home.html', title='Home:',tickets=all_tickets)


if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
