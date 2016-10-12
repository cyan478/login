#9/28
from flask import Flask, render_template, request, session, url_for, redirect
from utils.authreader import  dic, availAlready, checkAcc, makeAcc
import hashlib, os

app = Flask(__name__)
app.secret_key=os.urandom(32)


@app.route("/")
@app.route("/login/")
def login():
    print request.headers
    if len(session.keys()) == 0:
        return render_template('login.html', message = "")
    else:
        return redirect(url_for('home'))
    

@app.route("/home/")
def home():
	print session['user']
	return render_template('home.html', uname = session['user'])

@app.route("/logout/")
def logout():
	if len(session.keys()) == 0:
		return redirect(url_for('login'))
	else:
		session.pop('user')
		return render_template('login.html', message="You have logged out.")


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
       if availAlready(user,pw) == False:
       	return render_template('loginstat.html', auth = False, message = "This username does not exist.")
       elif availAlready(user,pw):
       	if checkAcc(user,pw) == False:
       		return render_template('loginstat.html', auth = False, message = "Your password is incorrect.")
       session['user'] = user		
       return redirect(url_for('home'))
        
   elif stat == 'Register':
    	if user == "" or pw == "": #CHECKING FOR STUPID ACTS
            return render_template('login.html', message = "Please fill in both fields.")
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
