def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove any unwanted characters or punctuation
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text

def extract_text_from_pdf(pdf_path):
    # Placeholder for PDF extraction logic
    pass

def check_adventure_in_text(text):
    # Check if the word "adventure" is in the text
    return "adventure" in text