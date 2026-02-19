
import sys
import pathlib

from pdf2image import convert_from_path
import pytesseract

# I need to get the name of the document from the
# command line arguments.

input_doc_name = sys.argv[1]

pages = convert_from_path(input_doc_name, dpi=600)
output_file = f"./output/{input_doc_name.replace('.pdf', '.txt')}"

pathlib.Path("./output").mkdir(exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        f.write(f"--- Page {i+1} ---\n")
        f.write(text + "\n")

