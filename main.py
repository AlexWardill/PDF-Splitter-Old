from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from Splitter import pdfSplitter

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "mvgtwiey4528wivndt6r89wjsnzgsoru56"
UPLOAD_FOLDER = "C:/Users/User/Downloads"
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'))
    return render_template('split.html')


@app.route("/about")
def about():
    return render_template('about.html')
    