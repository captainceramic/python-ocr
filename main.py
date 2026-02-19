from pdf2image import convert_from_path
import pytesseract

pages = convert_from_path("./docs/Mulesing article.pdf", dpi=600)

output_file = "output.txt"


with open(output_file, "w", encoding="utf-8") as f:
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        f.write(f"--- Page {i+1} ---\n")
        f.write(text + "\n")

