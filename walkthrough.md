# AI Legal Contract Intelligence Platform
## Comprehensive Technical Walkthrough

Now that your project is fully optimized and running smoothly, here is a detailed breakdown of how your application processes a legal contract from start to finish!

### 1. Document Ingestion ([document_ingestion.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/document_ingestion.py))
Everything starts when the user uploads a PDF or DOCX file to the Streamlit app.
- **Text Extraction:** The [DocumentProcessor](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/document_ingestion.py#10-38) uses `PyMuPDF` to read raw text from PDFs. For Word documents, it uses `python-docx`.
- **OCR Fallback:** If the PDF is scanned (an image without selectable text), the processor automatically detects that the extracted text is too short and falls back to Optical Character Recognition (OCR) using `Tesseract` to read the text off the images.

### 2. Clause Analysis & Extraction ([clause_analysis.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/clause_analysis.py))
Once it has the raw text, the system needs to understand the contract's structure.
- **Sentence Splitting:** It uses `spaCy` (a powerful NLP library) to structurally divide the massive wall of text into distinct sentences.
- **Classification:** It then reviews each sentence to classify what type of legal clause it is (e.g., *Confidentiality*, *Termination*, *Payment*). It does this using a two-pronged approach:
  1. **Regex Rules:** Looking for strict legal keywords (e.g., "indemnify").
  2. **Semantic Similarity:** Using a Hugging Face `SentenceTransformer` (`all-MiniLM-L6-v2`) to see if the sentence "means" the same thing as predefined example clauses, even if the exact keywords aren't present.

### 3. Risk Analysis ([risk_analysis.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/risk_analysis.py))
With the document neatly separated into labeled clauses, the system evaluates danger zones.
- The [RiskAnalyzer](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/risk_analysis.py#1-25) scans each clause for specific trigger keywords (like "breach", "penalty", or "liability") and assigns a risk score and severity level (Low, Medium, High). These flagged items appear in the Streamlit UI to give the user immediate warning of dangerous terms.

### 4. Knowledge Graph & Scenario Engine ([knowledge_graph.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/knowledge_graph.py), [scenario_engine.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/scenario_engine.py))
Behind the scenes, the app builds a relational web of data.
- It maps out how clauses relate to named entities (people, dates, organizations) extracted by `spaCy`, and connects them to potential outcomes simulated by the [ScenarioEngine](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/scenario_engine.py#1-20) (e.g., "Late salary payment → Employer faces penalties"). This forms a Backend Knowledge Graph using `NetworkX` that is ripe for future visual expansions.

### 5. RAG Retrieval System ([rag_qa.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/rag_qa.py))
This is the "Brain's Search Engine". When you ask the chatbot a question, it cannot memorize the whole document at once. 
- **Embeddings:** The [RAGQASystem](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/rag_qa.py#4-23) uses a `SentenceTransformer` to turn every single clause in the contract into a mathematical vector (an embedding).
- **Semantic Search:** When you ask, *"What happens if I quit?"*, it turns your question into a vector and mathematically calculates which 15 clauses in the contract are the most closely related in *meaning*. It pulls only those specific, highly relevant clauses.

### 6. The AI Agent ([hf_agent.py](file:///c:/Users/Lenovo/OneDrive/Desktop/Ai%20legal/hf_agent.py))
This is the "Brain's Voice". 
- Instead of using a simple summarizer, we upgraded your app to use **Meta's Llama-3 (8 Billion parameters)**, accessed live via the Hugging Face `InferenceClient`.
- **Prompt Engineering:** The agent receives a strict system prompt instructing it to act as an expert legal assistant. 
- **The Magic:** We feed the AI Agent the exact, highly-relevant clauses found by the RAG system, along with your original question. The AI Agent reads these specific clauses and synthesizes a perfect, human-readable answer grounded *entirely* in your document's text, preventing it from making up false legal advice!

---
**Summary:** You have built an enterprise-ready pipeline! You take unstructured data (PDFs) -> extract and classify it (SpaCy) -> embed it for searchability (RAG) -> and use cutting-edge LLMs (Llama-3) to interactively reason over the text.
