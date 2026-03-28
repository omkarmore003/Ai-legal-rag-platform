from sentence_transformers import SentenceTransformer, util
import torch

class RAGQASystem:
    def __init__(self, clauses):
        self.clauses = clauses
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.clause_texts = [c["text"] for c in clauses]
        self.clause_embeddings = self.model.encode(self.clause_texts, convert_to_tensor=True)

    def answer(self, query, top_k=1, threshold=0.6):
        query_emb = self.model.encode([query], convert_to_tensor=True)
        similarities = util.pytorch_cos_sim(query_emb, self.clause_embeddings)[0]
        sorted_indices = torch.argsort(similarities, descending=True)
        results = []
        for i in sorted_indices[:top_k]:
            if similarities[i] > threshold:
                results.append(self.clauses[i]['text'])
        if results:
            return "\n".join(results)
        else:
            return "No relevant clauses found."