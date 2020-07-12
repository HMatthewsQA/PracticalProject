from flask import Flask, render_template, redirect, url_for, request, Response
import requests
import random
import string

app = Flask(__name__)

@app.route('/letterstring', methods=['GET'])
def letterstring():
	letters = string.ascii_lowercase
	letterstring = ''.join(random.choice(letters) for i in range(8))
	return Response(letterstring, mimetype='text/plain')

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5001)
