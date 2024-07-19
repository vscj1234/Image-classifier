# create_database.py

from langchain_community.vectorstores import Chroma

CHROMA_PATH = "/content/chroma_db"

def save_to_chroma(chunks, embedding_function):
    # Initialize Chroma database
    db = Chroma(embedding_function=embedding_function, persist_directory=CHROMA_PATH)

    # Add or update chunks in the database
    for chunk in chunks:
        chunk_id = chunk.metadata['id']
        # Perform a search to check for existence
        search_results = db.similarity_search(chunk_id, k=1)

        if not search_results:
            # Add new chunk if not found
            db.add_documents([chunk], ids=[chunk_id])
            print(f"Added chunk {chunk_id}")
        else:
            # Assuming we can only add and can't truly update; add again
            db.add_documents([chunk], ids=[chunk_id])
            print(f"Updated chunk {chunk_id}")

    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def generate_data_store():
    documents = load_documents()
    if not documents:
        print("No documents found. Exiting.")
        return
    chunks = split_text(documents)
    if not chunks:
        print("No chunks generated. Exiting.")
        return
    save_to_chroma(chunks, get_embedding_function())
