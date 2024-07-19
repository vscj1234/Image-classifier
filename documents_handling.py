# document_handling.py

import os
import shutil
import fitz
from langchain.schema import Document

DATA_PATH = "/home"

def setup_data_directory():
    # Create the directory if it doesn't exist
    os.makedirs(DATA_PATH, exist_ok=True)

def upload_files():
    # Upload files
    uploaded = files.upload()

    # Move uploaded files to the data directory
    for filename in uploaded.keys():
        shutil.move(filename, os.path.join(DATA_PATH, filename))

def load_documents():
    # Load PDF documents from the directory
    documents = []
    for filename in os.listdir(DATA_PATH):
        if filename.endswith(".pdf"):
            filepath = os.path.join(DATA_PATH, filename)
            with fitz.open(filepath) as doc:
                for page_number, page in enumerate(doc, start=1):
                    text = page.get_text()
                    # Create Document object
                    document = Document(page_content=text, metadata={"source": filepath, "page": page_number})
                    documents.append(document)
    print(f"Loaded {len(documents)} documents.")
    return documents
