#9/28
from flask import Flask, render_template, request
from utils.authreader import readIn, dic, availAlready, checkAcc, makeAcc
import hashlib

app = Flask(__name__)



@app.route("/")
@app.route("/login/")
def login():
    print request.headers
    return render_template('login.html', message = "")

@app.route("/authenticate/", methods = ['GET','POST'])
def auth():
   print request.headers
   print request.form

   user = request.form['user'] 
   pw = request.form['password']
   pw = hashlib.sha224(pw).hexdigest() #hashed
   stat = request.form['account']

   if stat == 'Login':
   	
       if user == "" or pw == "": #CHECKING FOR STUPID ACTS
           return render_template('login.html', message = "Both fields must be filled out.")
       readIn()
       if availAlready(user,pw) == False:
       	return render_template('loginstat.html', auth = False, message = "This username does not exist.")
       elif availAlready(user,pw):
       	if checkAcc(user,pw) == False:
       		return render_template('loginstat.html', auth = False, message = "Your password is incorrect.")
       		
       return render_template('loginstat.html', auth = True)
        
   elif stat == 'Register':
    	
        if user == "" or pw == "": #CHECKING FOR STUPID ACTS
            return render_template('login.html', message = "Please fill in both fields.")
        readIn()
        if availAlready(user,pw):
            return render_template('login.html', message = "That username already exists. Please use another one.")
        elif availAlready(user,pw) == False:
            print availAlready(user,pw)
            makeAcc(user,pw)
            print dic
            
        return render_template('login.html', message = "Your account was successfully made! Login below.")

if __name__ == "__main__":
    app.debug = True
    app.run()
