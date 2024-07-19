# main.py

from setup_environment import *
from document_handling import *
from create_database import *
from query_data import *

if __name__ == "__main__":
    setup_data_directory()
    upload_files()
    generate_data_store()

    # Example query
    query_text = "What services do you offer?"
    query_database(query_text, get_embedding_function())
