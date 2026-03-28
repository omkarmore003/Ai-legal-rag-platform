import fitz  # PyMuPDF
from docx import Document
import pytesseract
from pdf2image import convert_from_path
import magic
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class DocumentProcessor:
    def __init__(self):
        self.file_type_detector = magic.Magic(mime=True)

    def process(self, file_path):
        file_type = self.file_type_detector.from_file(file_path)
        if 'pdf' in file_type:
            return self._process_pdf(file_path)
        elif 'word' in file_type or file_path.endswith('.docx'):
            return self._process_docx(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def _process_pdf(self, file_path):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        if len(text.strip()) < 100:
            images = convert_from_path(file_path, dpi=200)
            for image in images:
                text += pytesseract.image_to_string(image) + "\n"
        return text

    def _process_docx(self, file_path):
        doc = Document(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text