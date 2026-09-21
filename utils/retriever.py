import os
from langchain_community.vectorstores import FAISS
# We use the Endpoint class to bypass local Windows DLL execution
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from utils.parser import load_and_chunk_transcripts
from dotenv import load_dotenv

load_dotenv()

def build_or_load_vector_store(vector_store_path="faiss_index"):
    # Using the exact same model, but executing on HF servers to bypass Windows!
    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    if os.path.exists(vector_store_path):
        print("Loading existing FAISS index...")
        vector_store = FAISS.load_local(
            vector_store_path, 
            embeddings, 
            allow_dangerous_deserialization=True
        )
        return vector_store
    else:
        print("Building new FAISS index from transcripts...")
        docs = load_and_chunk_transcripts()
        
        if not docs:
            raise ValueError("No documents generated. Check the 'data' folder and regex.")
            
        vector_store = FAISS.from_documents(docs, embeddings)
        vector_store.save_local(vector_store_path)
        return vector_store

def get_retriever():
    vector_store = build_or_load_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": 20})

if __name__ == "__main__":
    retriever = get_retriever()
    print("Vector store ready!")