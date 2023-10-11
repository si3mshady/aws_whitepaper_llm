import os
from PyPDF2 import PdfReader
import csv
import re

# Define the input directory containing PDF files and the output CSV file
input_directory = "."
output_csv_file = "output.csv"

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

# Function to process PDFs in the directory and generate the CSV
def process_pdfs_and_generate_csv(input_directory, output_csv_file):
    with open(output_csv_file, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Title", "Content", "Category"])

        # Iterate through PDF files in the input directory
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_path = os.path.join(root, file)
                    title = os.path.splitext(file)[0]  # Use filename as title
                    content = extract_text_from_pdf(pdf_path)
                    category = "General"

                    # Write the data to the CSV file
                    csv_writer.writerow([title, content, category])

if __name__ == "__main__":
    process_pdfs_and_generate_csv(input_directory, output_csv_file)
