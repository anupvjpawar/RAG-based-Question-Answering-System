# RAG-based Question Answering System

This project implements a **RAG (Retriever-augmented Generation) based Question Answering System** using the **Transformers library** from Hugging Face. It includes a **Streamlit** web interface for interacting with the model, allowing users to input questions and receive answers based on a custom knowledge base.

## Features

- **Retriever-augmented Generation (RAG)**: Combines document retrieval and text generation to answer questions.
- **Streamlit Web Interface**: Simple web interface where users can ask questions and receive answers.
- **Custom Knowledge Base**: Uses a local text file (`knowledge_base.txt`) as the source of information for retrieval.

## Demo

You can run the app locally and ask questions like:
- **Who is Shiva?**
- **What is the Tandava dance?**

## Project Structure

```bash
.
├── rag_qa_streamlit.py       # Main Streamlit application
├── knowledge_base.txt        # Custom knowledge base (text file)
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies for the project
```
# Getting Started

## Prerequisites

Python 3.8 or above
Install the required dependencies from requirements.txt
Dependencies

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/rag-streamlit-app.git
   cd rag-streamlit-app
   ```

   

    
