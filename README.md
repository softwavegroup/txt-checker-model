# BERT Text Checker

This project utilizes a BERT mini model to check text extracted from PDF files for the presence of the word "adventure". 

## Project Structure

```
bert-text-checker
├── src
│   ├── main.py          # Entry point of the application
│   ├── bert_model.py    # Contains the BERT model class
│   ├── pdf_reader.py     # Handles reading PDF files
│   └── utils.py         # Utility functions for text processing
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Files to ignore in Git
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bert-text-checker.git
   cd bert-text-checker
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your PDF files in a directory.
2. Run the application:
   ```
   python src/main.py path/to/your/file.pdf
   ```

3. The application will output whether the word "adventure" is present in the text extracted from the PDF.

## BERT Model

This project uses the BERT mini model from the Hugging Face Transformers library. The model is designed for efficient text analysis and is capable of understanding context within the text.

## License

This project is licensed under the MIT License - see the LICENSE file for details.