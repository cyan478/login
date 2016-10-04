#9/28
from flask import Flask, render_template, request
from utils.authreader import readIn, dic, availAlready, makeAcc
import hashlib

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def login():
    print request.headers
    return render_template('login.html', message = "")

@app.route("/authenticate/", methods = ['POST'])
def auth():
   print request.headers
   print request.form
   user = "hello"
   pw = "itsme"
   auth = (request.form['user'] == user and request.form['password'] == pw)
   #return render_template('login.html', message = auth)
   return render_template('loginstat.html', auth = auth)

@app.route("/register/")
def register():
	print request.headers
	return render_template('register.html', message = "")

@app.route("/rauthenticate/", methods = ['POST'])
def rauth():
   print request.headers
   print request.form

   user = request.form['user'] 
   pw = request.form['password']
   pw = hashlib.sha224(pw).hexdigest() #hash it!!!!

   readIn()
   if availAlready(user,pw):
   	return render_template('register.html', message = "That username already exists. Please use another one.")

   elif availAlready(user,pw) == False:
   	print availAlready(user,pw)
   	makeAcc(user,pw)
   	print dic

   #auth = (request.form['user'] == user and request.form['password'] == pw)
   #return render_template('loginstat.html', auth = auth)
   return render_template('login.html', message = "Your account was successfully made! Login below.")


if __name__ == "__main__":
    app.debug = True
    app.run()
