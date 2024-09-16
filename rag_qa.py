import torch
from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration
import faiss
from datasets import Dataset
import os
import streamlit as st

# 1. Load or create a knowledge base
def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        texts = file.readlines()
    return texts

# 2. Prepare the dataset for retrieval
def prepare_dataset(texts):
    dataset = Dataset.from_dict({"text": texts})
    return dataset

# 3. Create FAISS Index (for demonstration, we'll skip the actual indexing here)
def create_faiss_index(dataset):
    d = 768  # Embedding size for BERT-based models
    index = faiss.IndexFlatL2(d)  # L2 distance metric
    return index

# 4. Set up RAG (Retriever-Generator)
def setup_rag_model():
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", use_dummy_dataset=True)
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)
    return tokenizer, retriever, model

# 5. Retrieve relevant documents and generate an answer
def generate_answer(query, tokenizer, retriever, model, device="cpu"):
    input_ids = tokenizer(query, return_tensors="pt").input_ids.to(device)
    generated = model.generate(input_ids, num_beams=2, max_length=200, early_stopping=True)
    return tokenizer.batch_decode(generated, skip_special_tokens=True)

# Streamlit Web Interface
def main():
    st.title("RAG-based Q&A System")
    st.write("Ask questions and get answers based on a custom knowledge base.")

    # Load knowledge base
    knowledge_base_file = "knowledge_base.txt"
    if not os.path.exists(knowledge_base_file):
        st.error(f"Knowledge base file '{knowledge_base_file}' not found!")
        return
    
    knowledge_texts = load_knowledge_base(knowledge_base_file)
    
    # Prepare dataset and FAISS index (optional step, kept simple here)
    dataset = prepare_dataset(knowledge_texts)
    faiss_index = create_faiss_index(dataset)
    
    # Set up RAG model
    tokenizer, retriever, model = setup_rag_model()
    model.to("cpu")  # Set to "cuda" if using GPU

    # User input for the question
    user_query = st.text_input("Enter your question:")
    
    if user_query:
        # Generate answer
        with st.spinner("Generating answer..."):
            answer = generate_answer(user_query, tokenizer, retriever, model, device="cpu")
        
        st
