# CogniCore - A 100% Local and Private RAG Assistant

Welcome to CogniCore, an enterprise-grade Retrieval-Augmented Generation (RAG) system designed to provide a secure, private, and intelligent interface to your local documents. This project runs entirely on your own hardware with no need for API keys or an internet connection after setup.

## The Problem
Enterprises and individuals have critical knowledge scattered across numerous documents. Using commercial AI services like ChatGPT to query this information raises major privacy concerns, as sensitive data must be sent to third-party servers. Furthermore, API costs can become prohibitive at scale.

## The Solution
CogniCore solves this by using powerful, open-source models that run directly on your CPU. It ingests your local documents (PDFs, Markdown), creates a private knowledge base, and allows you to ask complex questions in natural language. Your data never leaves your machine.

---
## Live Demo
A quick look at the CogniCore assistant answering a question about the internal HR policy.

![CogniCore Demo Screenshot](https://raw.githubusercontent.com/aaronseq12/cognicore-local-rag-assistant/main/demo.png)
---

## Tech Stack & Architecture
CogniCore is built with a modern, modular Python stack designed for local execution.

* **Orchestration Framework:** `LangChain`
* **Large Language Model (LLM):** `Microsoft Phi-3-mini` (running via `llama-cpp-python`)
* **Embedding Model:** `all-MiniLM-L6-v2` (running via `sentence-transformers`)
* **Vector Database:** `ChromaDB` for local, on-disk storage.
* **Backend API:** `FastAPI`
* **Frontend UI:** `Streamlit`

**Flow:**
1.  Documents are loaded and split into chunks.
2.  Chunks are converted to vector embeddings and stored in a local ChromaDB.
3.  A user asks a question via the Streamlit UI.
4.  The question is embedded, and a similarity search retrieves the most relevant chunks from the database.
5.  The question and retrieved chunks are passed to the local Phi-3 LLM to generate a final answer.

---

## How to Run Locally

Follow these steps to get CogniCore running on your own machine.

**1. Clone the Repository:**
```bash
git clone [https://github.com/your-username/cognicore_local.git](https://github.com/your-username/cognicore_local.git)
cd cognicore_local
```

**2. Set Up a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```
*(Note: If `llama-cpp-python` fails to build on Windows, you will need to install the C++ Build Tools from Visual Studio.)*

**4. Download the LLM Model:**
- Download the model file `Phi-3-mini-4k-instruct-q4.gguf` from [Hugging Face](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf).
- Create a `models` folder in the project root and place the downloaded file inside it.

**5. Add Your Data:**
- Place the PDF and Markdown documents you want to query inside the `src/data` folder.

**6. Create the Knowledge Base:**
- Run the ingestion script once. This will process your data and create a `chroma_db` folder.
```bash
python src/core/ingestion.py
```

**7. Run the Application:**
- **Terminal 1: Start the Backend**
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```
- **Terminal 2: Start the Frontend**
```bash
streamlit run src/ui.py
```
- Your application will now be running in your browser!
