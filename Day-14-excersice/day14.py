from flask import Flask, render_template,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return "This is the Index page"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/members')
def memebers():
    return "Members Page"

@app.route("/q2/<mark>")
def hello_world(mark):
    return render_template('index.html',mark=int(mark))

if __name__== "__main__":
    app.run()