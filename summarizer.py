from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_contract(text):
    if len(text) > 1000:
        text = text[:1000]
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]['summary_text']