
****This project has been folded into "TDL KAIZEN". Please see that page instead. 

# BPER PDF Splitter

## Overview
This Python script utilizes PyMuPDF to parse through a BPER 'detailed PDF' bulk download and break it into separate BPER documents. It identifies the start of each new BPER section by searching for a unique text marker and then splits the file, renaming each section based on a specific BPER identifier found in the text.

## Features
- **PDF Parsing**: Efficiently parses through large PDF files.
- **Text-Based Splitting**: Splits the PDF file each time a specific text marker ("TDL Control:") is encountered.
- **Dynamic Renaming**: Renames each split document based on a wildcard search for "BPER*****" within the text.

## Prerequisites
- Python 3.x
- PyMuPDF (fitz)
- Regular Expressions (re)

You can install PyMuPDF using pip:
```bash
pip install pymupdf
```

## Usage
To use the script, simply pass the filename of the PDF you want to split as a command-line argument:

```bash
python BPERsorter.py path_to_your_pdf.pdf
```

## How It Works
- **Extracting BPER Name**: Searches for the pattern "BPER*****" on each page where "TDL Control:" is found to determine the new file's name.
- **Splitting PDF**: Iterates through the PDF; when "TDL Control:" is encountered, it starts a new document from that page onwards.
- **Saving Files**: Each split document is saved with the extracted BPER name. If the BPER name is not found, it defaults to 'rename_me'.

