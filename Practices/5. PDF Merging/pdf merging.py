from pypdf import PdfWriter
import os

files = [files for files in os.listdir() if files.endswith(".pdf")]
merger = PdfWriter()

for pdf in files:    
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()