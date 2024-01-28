from flask import Flask

app = Flask(__name__)

@app.route('/home') #Basic route 
def index(): #View function
    return "Hello World!"


if __name__ =="__main__":
    app.run(debug=True)