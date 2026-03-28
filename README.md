# 📑 AI Legal Contract Intelligence Platform

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-yellow)
![RAG](https://img.shields.io/badge/Architecture-RAG-success.svg)

An intelligent, end-to-end **Retrieval-Augmented Generation (RAG)** pipeline designed to ingest, analyze, and intelligently converse with legal contracts (PDF/DOCX) using advanced Natural Language Processing (NLP) and Meta's Llama-3 Large Language Model.

## ✨ Key Features
- **Intelligent Ingestion:** Automatically extracts text from PDFs and DOCX files. Includes an automated Optical Character Recognition (OCR) fallback for scanned images using Tesseract.
- **Automated Clause Analysis:** Utilizes `spaCy` to structurally break down dense legal jargon into categorized sentences (e.g., Confidentiality, Termination, Payment).
- **Risk Assessment:** Programmatically scans and flags high, medium, and low-risk terminologies inside the contract.
- **Semantic Vector Search (The "R" in RAG):** Embedded with `SentenceTransformers`. Converts clauses into mathematical vectors to perform deep-meaning semantic searches based on user queries, retrieving highly specific context.
- **Conversational AI Agent (The "A.G." in RAG):** Powered by `Meta-Llama-3-8B-Instruct` via the Hugging Face Inference API. It provides human-like, conversational legal answers grounded *strictly* in the retrieved clauses of your uploaded contract to prevent hallucinated legal advice.
- **Beautiful UI:** Wrapped in an intuitive `Streamlit` frontend web application.

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Document Processing:** PyMuPDF (`fitz`), `python-docx`, `pytesseract`, `pdf2image`
* **NLP & Chunking:** `spaCy` (`en_core_web_sm`)
* **Embeddings & Vector Search:** `sentence-transformers` (`all-MiniLM-L6-v2`), PyTorch
* **LLM Integration:** `huggingface_hub` (InferenceClient), `python-dotenv`

---

## 🚀 Getting Started

### 1. Prerequisites
You will need Python 3.10+ installed on your machine.
If you want the OCR fallback to work on scanned PDFs, you must have [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) installed on your system.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/yourusername/Ai-legal-platform.git
cd Ai-legal-platform

# Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
This project uses the Hugging Face Serverless Inference API for the Llama-3 model. You will need a free HF API Token.
1. Get a free token from [Hugging Face Settings](https://huggingface.co/settings/tokens).
2. Ensure you check the **"Make calls to Inference Providers"** permission.
3. Create a `.env` file in the root directory and add your key:
```env
HUGGINGFACE_API_KEY=your_token_here
```

### 4. Running the Application
Start the Streamlit application by running:
```bash
streamlit run app.py
```
The application will automatically open in your default web browser at `http://localhost:8501`.

---

## 🧠 How the RAG Pipeline Works
1. **Upload:** User uploads a dense legal contract.
2. **Retrieve:** The system breaks the document into semantic chunks (clauses). When a user asks a question, the vector search engine retrieves the top 15 most relevant clauses related to that specific question.
3. **Augment & Generate:** The 15 retrieved clauses are bundled perfectly into a background prompt along with the user's question, and sent to the LLM (Llama-3). The agent reads the strict legal text and translates it into a friendly, accurate answer.

---

*Disclaimer: This tool is a software demonstration of an AI RAG pipeline and should not be used as a substitute for professional legal counsel.*
