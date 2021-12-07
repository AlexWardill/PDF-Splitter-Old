from flask import Flask, render_template
from simple import write_n_lines

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('base.html')

@app.route("/split")
def split():
    return render_template('split.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/write-lines")
def writeLines():
    return
