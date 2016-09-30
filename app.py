#9/28
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def login():
    print request.headers
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST'])
def auth():
   print request.headers
   print request.form
   #print request.form['user']
   #print request.form['password']
   user = "hello"
   pw = "itsme"
   if (request.form['user'] == user and request.form['password'] == pw):
   		return "Successful login!! Welcome"
   else:
    	return "Unsucessful login"


if __name__ == "__main__":
    app.debug = True
    app.run()
