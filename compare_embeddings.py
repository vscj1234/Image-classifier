# compare_embeddings.py

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(documents):
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,  # Increase chunk size for more content
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # Add unique ID to each chunk
    chunk_id_counter = {}
    for chunk in chunks:
        source = chunk.metadata.get('source', 'unknown')
        page_number = chunk.metadata.get('page', 0)
        if (source, page_number) not in chunk_id_counter:
            chunk_id_counter[(source, page_number)] = 0
        chunk_index = chunk_id_counter[(source, page_number)]
        chunk.metadata['id'] = f"{source}-page{page_number}-chunk{chunk_index}"
        chunk_id_counter[(source, page_number)] += 1

    return chunks

def get_embedding_function():
    """Return an OpenAI embedding function."""
    return OpenAIEmbeddings()
