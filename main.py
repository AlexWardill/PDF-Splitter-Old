from flask import Flask, render_template, request, make_response, redirect, url_for
from Splitter import pdfSplitter

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "mvgtwiey4528wivndt6r89wjsnzgsoru56"

@app.route("/")
def split():
    return render_template('split.html')

@app.route("/", methods=["GET", "POST"])
def split_file():
    if request.method == "POST":
        the_request = request.files
        print(f"request IS {the_request}")
        # input_file = request.files["input_file"]
        # pdfSplitter(file)
    return redirect(url_for('split'))



@app.route("/about")
def about():
    return render_template('about.html')
    