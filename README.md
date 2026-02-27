# Fake News Detection System

**Author:** Mannuru Lucky Balaji (2300030405)

## 1. Project Overview
The Fake News Detection System is a Machine Learning-based web application developed to automatically identify whether a news article is real or fake. With the rapid growth of digital media platforms and social networks, misinformation spreads quickly, causing confusion and societal harm. This project aims to tackle that issue using Natural Language Processing (NLP) and supervised machine learning techniques.

## 2. System Architecture
The application follows a modular architecture consisting of three phases: Ingestion, Storage, and Retrieval.
*   **Frontend:** FastAPI-hosted HTML interface for file uploads and chat interaction. (Note: Also uses Streamlit for simple interfaces.)
*   **Backend:** FastAPI server handling processing and API routing.
*   **Vector Database:** ChromaDB Cloud for storing and querying embeddings.
*   **LLM Engine:** Ollama (llama3.2:1b model) for generating context-based responses.

## 3. Technical Implementation
*   **Data Ingestion & Extraction:** Uses pypdf, python-docx, pandas, and BeautifulSoup for extracting and converting content.
*   **Embedding & Vectorization:** Text is chunked (1000 characters with 100 overlap) and converted into vectors using all-MiniLM-L6-v2 (Sentence-Transformers), stored in ChromaDB with source_id management.
*   **RAG Pipeline:** User query is vectorized, top 5 relevant chunks are retrieved, injected as context, and processed by llama3.2:1b to generate answers strictly from retrieved data.

## 4. Key Features
1.  **Multi-Format Support** for structured and unstructured data.
2.  **Dynamic Source Management** using source_id.
3.  **Asynchronous API** built on FastAPI.
4.  **Local LLM Integration** using Ollama without external API dependency.

## 5. Conclusion and Future Scope
The Fake News Detection system successfully identifies whether a news article is real or fake using Machine Learning and Natural Language Processing (NLP) techniques. By preprocessing textual data and applying classification algorithms, the model is able to learn patterns from the dataset and provide accurate predictions. The Streamlit-based interface makes the system simple, interactive, and easy to use for anyone. This project demonstrates how artificial intelligence can play a significant role in reducing the spread of misinformation online. 

In the future, advanced deep learning models such as LSTM or BERT can be implemented to improve contextual understanding and accuracy. The system can also be expanded to support multiple languages and integrated with real-time news APIs for live verification. Additionally, image and video fake detection features can be included to handle multimedia misinformation. With continuous improvements and enhancements, the system has the potential to become a powerful and reliable tool in combating fake news.
