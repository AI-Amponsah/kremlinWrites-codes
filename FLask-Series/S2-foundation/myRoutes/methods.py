#This is for reference.
from flask import Flask,request
app= Flask(__name__)

@app.route('/home', methods=['GET'])
def index():
	return 'I am exploring HTTP methods with flask routes'



@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=='POST':
		return 'Form submitted successfully'
	elif request.method=='GET':
	    return 'user profile'
	
    