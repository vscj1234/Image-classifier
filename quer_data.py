# query_data.py

from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def query_database(query_text, embedding_function):
    # Prepare the DB
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB
    results = db.similarity_search_with_relevance_scores(query_text, k=5)
    if len(results) == 0 or results[0][1] < 0.7:
        print("Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _ in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)

# Example query
query_text = "What services do you offer?"
query_database(query_text, get_embedding_function())
