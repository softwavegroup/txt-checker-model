from bert_model import BertModel
from pdf_reader import PdfReader

def main():
    # Initialize the BERT model
    bert_model = BertModel()

    # Read the PDF file
    pdf_reader = PdfReader()
    pdf_text = pdf_reader.read_pdf('text checker/Adventure-01-The-Island-of-Adventure-Enid-Blyton.pdf')

    # Check for the word "adventure"
    if bert_model.check_for_adventure(pdf_text):
        print("The word 'adventure' is present in the text.")
    else:
        print("The word 'adventure' is not found in the text.")

if __name__ == "__main__":
    main()