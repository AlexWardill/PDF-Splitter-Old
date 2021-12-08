from flask import Flask, render_template, request, make_response
from Splitter import pdfSplitter

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "mvgtwiey4528wivndt6r89wjsnzgsoru56"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        the_request = request.files
        print(f"REQUEST IS {the_request}")
        input_file = request.files["input_file"]
        pdfSplitter(input_file)
    return render_template('split.html')


@app.route("/about")
def about():
    return render_template('about.html')
    