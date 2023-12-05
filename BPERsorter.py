#This script uses PyMuPDF to parse a BPER 'detailed PDF' bulk download and break it into separate BPER's. It does so by parsing through the pdf, finding text that should be unique to the first page of the BPER, then splitting off the file and renaming it from a wildcard search for BPER***** on that page. -MB
#Pass arugments on command line like this 'python BPERsorter.py filename'

import fitz  # aka PyMuPDF, use 'pip install library x' at the command line if you don't have these libraries 
import re
import sys

#function for extracting the BPER name
def extract_bper_text(page_text):
    match = re.search(r'BPER\d+', page_text)
    return match.group(0) if match else 'rename_me'

#function for splitting off the pdf
def split_pdf(input_pdf):
    pdf_document = fitz.open(input_pdf)
    current_output = None
    output_name = None
    page_count = 0
    #loops through the pdf and grabs the text we want
    for page in pdf_document:
        page_text = page.get_text()

        if "TDL Control:" in page_text:
            if current_output:
                current_output.save(f'{output_name}.pdf')
            current_output = fitz.open()
            output_name = extract_bper_text(page_text)
            page_count = 0

        if current_output is not None:
            current_output.insert_pdf(pdf_document, from_page=page.number, to_page=page.number)
            page_count += 1

    # save it as the BPER name if there is a page grabbed and then close the new file
    if current_output and page_count > 0:
        current_output.save(f'{output_name}.pdf')

    pdf_document.close()

# execution and sexy command line argument so we don't have to keep changing the file path
if len(sys.argv) > 1:
    split_pdf(sys.argv[1])
else:
    print("Please provide a PDF file path")