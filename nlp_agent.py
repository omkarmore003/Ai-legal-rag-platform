from transformers import pipeline

class NLPLegalAgent:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model="google/flan-t5-base")

    def answer(self, question, clauses):
        context = " ".join([c['text'] for c in clauses])
        prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
        result = self.generator(prompt, max_length=128, do_sample=False)
        return result[0]['generated_text']