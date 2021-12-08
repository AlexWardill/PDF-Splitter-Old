from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

def pdfSplitter(big_pdf_name):
    pdf_path = (
            Path.home()
            / "PycharmProjects"
            / "PDFSplitter"
            / f"{big_pdf_name}"
    )
    input_pdf = PdfFileReader(str(pdf_path))

    for i in range(input_pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(input_pdf.getPage(i))
        with Path(f"output_files/page {i+1}.pdf").open(mode="wb") as output_file:
            pdf_writer.write(output_file)
    return 0