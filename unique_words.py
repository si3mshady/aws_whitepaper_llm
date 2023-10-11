import os
from PyPDF2 import PdfReader
import re

# Define the input directory containing PDF files and the output text file
input_directory = "."
output_text_file = "output.txt"

# Function to extract text from a PDF file and clean the text
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf = PdfReader(pdf_path)
    for page in pdf.pages:
        text += page.extract_text()
    
    # Remove multiple spaces and ellipses
    text = re.sub(r'\s+', ' ', text)          # Replace multiple spaces with a single space
    text = re.sub(r'\.{2,}', '', text)        # Remove ellipses
    text = re.sub(r',', '', text)             # Remove commas
    text = re.sub(r'\.', '', text)            # Remove periods
    text = re.sub(r'-', '', text)             # Remove dashes
    text = text.strip()                       # Remove leading/trailing spaces
    
    return text

# Function to process PDFs in the directory and generate the text file
def process_pdfs_and_generate_text(input_directory, output_text_file):
    unique_words = set()  # Create a set to store unique words
    
    # Iterate through PDF files in the input directory
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                print(f"Processing {file}...")
                text = extract_text_from_pdf(pdf_path)
                
                # Tokenize the text into words using regular expressions
                words = re.findall(r'\b\w+\b', text.lower())
                unique_words.update(words)

    # Write the unique words to the text file
    with open(output_text_file, "w", encoding="utf-8") as text_file:
        for word in unique_words:
            text_file.write(word + "\n")

if __name__ == "__main__":
    process_pdfs_and_generate_text(input_directory, output_text_file)
