from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def ask_hf_agent(question, context, model="meta-llama/Meta-Llama-3-8B-Instruct"):
    client = InferenceClient(model, token=HUGGINGFACE_API_KEY)
    
    # Improved Prompt Engineering for Instruct Models
    system_prompt = "You are an expert legal assistant. Answer the user's question using ONLY the provided legal clauses below. If the answer is not contained in the provided clauses, say 'I cannot find the answer to this in the contract'."
    
    user_prompt = f"Contract Clauses:\n{context}\n\nQuestion: {question}"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = client.chat_completion(messages, max_tokens=250)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error connecting to AI Agent: {str(e)}"