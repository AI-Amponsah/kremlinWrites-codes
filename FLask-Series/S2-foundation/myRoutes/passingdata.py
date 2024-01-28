from flask import Flask, request

app= Flask(__name__)

@app.route('/home/<username>',methods=['GET'])
def index(username):
	return username


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    # Handle user profile for the specified user ID (integer)
    return f" User Profile for ID {user_id}"