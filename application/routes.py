from flask import render_template, redirect, url_for, request
from application import app, db
#from application.models

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home:')