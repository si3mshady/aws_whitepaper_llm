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
    
    return text

# Function to process PDFs in the directory and generate the text file
def process_pdfs_and_generate_text(input_directory, output_text_file):
    # Create a list to store text from all PDFs
    all_texts = []
    
    # Iterate through PDF files in the input directory
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                print(f"Processing {file}...")
                text = extract_text_from_pdf(pdf_path)
                all_texts.append(text)

    # Combine all text into one string
    combined_text = ' '.join(all_texts)

    # Clean the combined text using regular expressions
    cleaned_text = re.sub(r'\s+', ' ', combined_text)  # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\.{2,}', '', cleaned_text)  # Remove ellipses
    cleaned_text = re.sub(r',', '', cleaned_text)  # Remove commas
    cleaned_text = re.sub(r'\.', '', cleaned_text)  # Remove periods
    cleaned_text = re.sub(r'-', '', cleaned_text)  # Remove dashes
    cleaned_text = cleaned_text.strip()  # Remove leading/trailing spaces

    # Write the cleaned text to the text file
    with open(output_text_file, "w", encoding="utf-8") as text_file:
        text_file.write(cleaned_text)

if __name__ == "__main__":
    process_pdfs_and_generate_text(input_directory, output_text_file)
