from flask import render_template, redirect, url_for, request, Response
import requests
import random

app = Flask(__name__)

@app.route('/primeno', methods='GET')
def primeno():
	primeno = random.randint(0,20)
	return Response(primeno, mimetype='text/plain')

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
