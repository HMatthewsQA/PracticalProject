from flask import Flask, render_template, redirect, url_for, request, Response
import requests
import random

app = Flask(__name__)

@app.route('/checkstring', methods=['POST'])
def checkstring():
	result=False
	checkstring = request.data.decode('utf-8')
	if (checkstring.find('A') != -1): 
		result=True
	elif (checkstring.find('a') != -1): 
		result=True
	else: 
		result=False
	return Response(result, mimetype='text/plain')

@app.route('/checkprime', methods=['POST'])
def checkprime():
	num = int(request.data.decode('utf-8'))
	isprime = False
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				isprime = False
				break
			else:
				isprime=True
	else:
		isprime = False
	return Response(isprime, mimetype='text/plain')

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5003)
