class PdfReader:
    def __init__(self):
        pass

    def read_pdf(self, pdf_path):
        from PyPDF2 import PdfReader as PyPDFReader

        text = ""
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDFReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()