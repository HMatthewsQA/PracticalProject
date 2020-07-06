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
	letterstring = requests.get('http://app2:5001/letterstring')
	primeno = requests.get('http://app3:5002/primeno')
	checkstring = requests.post('http://app4:5003/checkstring', data=letterstring)
	checkprime = requests.post('http://app4:5003/checkprime', data=primeno)
	return render_template('home.html', title='Home:')


if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
