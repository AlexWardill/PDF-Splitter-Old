from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
from flask import request

def pdfSplitter(target_pdf):
    pdf_path = (
            Path.home()
            / "Downloads"
            / f"{target_pdf}"
    )
    input_pdf = PdfFileReader(str(pdf_path))

    
    for i in range(input_pdf.getNumPages()):
        response = PdfFileWriter()
        response.addPage(input_pdf.getPage(i))
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        print(response)
        return response
    # for i in range(input_pdf.getNumPages()):
    #     pdf_writer = PdfFileWriter()
    #     pdf_writer.addPage(input_pdf.getPage(i))
    #     with Path(f"Downloads/{target_pdf} page {i+1}.pdf").open(mode="wb") as output_file:
    #         pdf_writer.write(output_file)
    #         print(pdf_writer)
    # return 0

    # return render_template('split.html')