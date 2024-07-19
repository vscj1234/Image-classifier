# setup_environment.py

import os
from google.colab import files
import shutil
import fitz  # PyMuPDF

from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate

# Constants
DATA_PATH = "/home"
CHROMA_PATH = "/content/chroma_db"  # Use a writable directory
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""
