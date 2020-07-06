from flask import render_template, redirect, url_for, request, Response
import requests
import random

app = Flask(__name__)

@app.route('/checkstring', methods='POST')
def checkstring():
	checkstring = request.data.decode('utf-8')
	return Response(result, mimetype='text/plain')

@app.route('/checkprime', methods='POST')
def checkprime():
	checkprime = request.data.decode('utf-8')
	return Response(result, mimetype='text/plain')

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
