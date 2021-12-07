from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<header>Index page</header>"

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def greeting(name=None):
    return render_template('greeting.html', name=name)

