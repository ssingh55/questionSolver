# backend/app.py
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/process_question_paper', methods=['POST'])
# def process_question_paper():
#     # Implement backend logic here
#     # Receive data from frontend and return processed results
#     return jsonify({"result": "Processed successfully"})

# backend/text_extraction.py
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

def process_image(image):
    # Extract text from the image using Tesseract OCR
    text = pytesseract.image_to_string(image)
    return text

def process_pdf(pdf_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Extract text from each image using Tesseract OCR
    text = ""
    for i, image in enumerate(images):
        text += f"Page {i + 1}:\n"
        text += pytesseract.image_to_string(image)
        text += "\n\n"

    return text

def process_uploaded_file(uploaded_file):
    if uploaded_file.type.startswith('image'):
        image = Image.open(uploaded_file)
        return process_image(image)
    elif uploaded_file.type == 'application/pdf':
        # Save the PDF temporarily
        pdf_path = "temp.pdf"
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(uploaded_file.read())

        # Process PDF and get the extracted text
        extracted_text = process_pdf(pdf_path)

        # Remove the temporary PDF file
        os.remove(pdf_path)

        return extracted_text
    else:
        return "Unsupported file type. Please upload a PDF or image."
