from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path


app = Flask(__name__)
# UPLOAD_FOLDER = "Downloads"
UPLOAD_FOLDER = "downloaded"
ALLOWED_EXTENSIONS = {'pdf'}
secret_key = os.urandom(12).hex()
app.config['SECRET_KEY'] = secret_key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

root_path = os.path.join(Path.home(), "src")

@app.route("/", methods=["GET", "POST"])
def upload_file():
    filelist = [ f for f in os.listdir(os.path.join(root_path, "downloaded")) if not f.endswith(".txt") ]
    for f in filelist:
        os.remove(os.path.join(root_path, "downloaded", f"{f}" ))

    if request.method == 'POST':
        # Check if user has uploaded a file
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # define file variable
        file = request.files['file']
        # check if file has non-empty file name
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # save inddividual pages from big_pdf
        if file and allowed_file(file.filename):
            big_pdf = PdfFileReader(file)
            for i in range(big_pdf.getNumPages()):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(big_pdf.getPage(i))
                
                # CREATE BLANK PDF IN DOWNLOADS FOLDER, THEN SET IT AS OUTPUT FILE
                # not accessing the actual Downloads path
                    # instead it's getting app/Downloads...
                            
                with Path(os.path.join(root_path, "downloaded"), f"page {i+1}.pdf").open(mode="wb+") as output_file:
                    pdf_writer.write(output_file)

                send_file(f"page {i+1}.pdf", as_attachment=True)
                    
            return redirect(url_for('upload_file'))
    return render_template('split.html')


@app.route("/about")
def about():
    return render_template('about.html')
    

if __name__ == '__main__':
    app.run()