import spacy
import re
import torch
from sentence_transformers import SentenceTransformer, util

class ClauseAnalyzer:
    def __init__(self, clauses=None):
        self.nlp = spacy.load("en_core_web_sm")
        self.clause_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.clauses = clauses if clauses else []
        self.clause_patterns = {
            "confidentiality": [r"confidential", r"non.?disclosure", r"nda"],
            "termination": [r"terminat(e|ion)", r"expir(e|ation)", r"cancel"],
            "indemnification": [r"indemnif(y|ication)", r"hold harmless"],
            "governing_law": [r"governing law", r"jurisdiction", r"arbitration"],
            "payment": [r"payment", r"compensation", r"salary", r"fees"],
        }
        self.clause_examples = {
            "confidentiality": [
                "The parties agree to keep all information confidential.",
                "Confidentiality obligations survive termination.",
            ],
            "termination": [
                "This agreement may be terminated by either party.",
                "Termination for cause shall be immediate.",
            ],
            "indemnification": [
                "Each party agrees to indemnify the other.",
                "The company shall hold the employee harmless.",
            ],
        }
        self.clause_embeddings = {
            ctype: self.clause_model.encode(examples)
            for ctype, examples in self.clause_examples.items()
        }

    def extract_clauses(self, text):
        doc = self.nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        clauses = []
        for i, sentence in enumerate(sentences):
            clause_type = self._classify_clause(sentence)
            if clause_type:
                clauses.append(
                    {
                        "text": sentence,
                        "type": clause_type,
                        "position": i,
                    }
                )
        self.clauses = clauses
        return clauses

    def _classify_clause(self, text):
        for clause_type, patterns in self.clause_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    return clause_type
        text_embedding = self.clause_model.encode([text])
        best_score, best_type = 0.7, None
        for clause_type, embeddings in self.clause_embeddings.items():
            similarities = util.cos_sim(text_embedding, embeddings)
            max_similarity = torch.max(similarities).item()
            if max_similarity > best_score:
                best_score, best_type = max_similarity, clause_type
        return best_type