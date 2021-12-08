from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "mvgtwiey4528wivndt6r89wjsnzgsoru56"

@app.route("/", methods=["GET", "POST"])
def home():
    
    return render_template('split.html')


@app.route("/about")
def about():
    return render_template('about.html')
    