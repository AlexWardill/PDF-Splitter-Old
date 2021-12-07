from flask import Flask, render_template, request, session
# from simple import write_n_lines
from adder import double

app = Flask(__name__)
app.config["SECRET_KEY"] = "mvgtwiey4528wivndt6r89wjsnzgsoru56"

@app.route("/", methods=["GET", "POST"])
def home():
    if "input" not in session:
        session["input"] = []

    errors = ""

    if request.method == "POST":
        number = None
        try:
            session["input"].append(int(request.form["number"]))
            session.modified = True
        except:
            errors += f"!{number} is not a number."
        if request.form.getlist("action")[0] == "Double it":
            result = double(session["input"][0])
            session["input"].clear()
            session.modified = True
            return render_template('split.html', errors=errors, result=result)
    return render_template('split.html', errors=errors, result=None)


@app.route("/about")
def about():
    return render_template('about.html')

