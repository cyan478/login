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
    print request.form['user']
    return "ok"

if __name__ == "__main__":
    app.debug = True
    app.run()
