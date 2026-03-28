import streamlit as st
from main import ContractAnalyzer
from summarizer import summarize_contract  # <-- Add this import
from hf_agent import ask_hf_agent

st.set_page_config(page_title="Legal Contract Intelligence Platform", layout="wide")
st.title("📑 Legal Contract Intelligence Platform")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

uploaded_file = st.file_uploader("Upload a contract (PDF or DOCX)", type=["pdf", "docx"])
if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    analyzer = ContractAnalyzer()
    clauses, risks, scenarios = analyzer.analyze_contract(uploaded_file.name)

    st.header("📝 Extracted Clauses")
    for clause in clauses:
        st.markdown(f"- **{clause.get('type', 'CLAUSE')}**: {clause['text']}")

    st.header("⚠️ Risks")
    for risk in risks:
        st.markdown(f"- **Risk ({risk['type']})**: {risk['text']} (score {risk['score']:.2f})")

    st.header("🔮 Scenario Simulations")
    for scenario in scenarios:
        st.markdown(f"- {scenario['scenario']} → {scenario['consequence']}")

    st.header("🤖 AI Legal Agent Chat")
    user_query = st.text_input("Ask a legal question or type commands like 'show high risk':")
    if user_query:
        # For general questions like "what is in this contract", we need more context than just 3 clauses
        # Lowering the threshold and increasing top_k gives the AI a broader overview of the document
        context = analyzer.rag_qa.answer(user_query, top_k=15, threshold=0.1)
        
        # Add a fallback if no relevant clauses are found to still allow the AI to answer generally or state it doesn't know
        if context == "No relevant clauses found.":
            context = "Provide a general legal answer or state that the contract doesn't contain this information."

        agent_answer = ask_hf_agent(user_query, context)
        answer = f"**AI Agent Answer:**\n{agent_answer}"
        st.session_state.conversation.append({"role": "user", "content": user_query})
        st.session_state.conversation.append({"role": "agent", "content": answer})
        st.info(answer)

    if st.session_state.conversation:
        st.markdown("---")
        st.subheader("Conversation History")
        for turn in st.session_state.conversation:
            if turn["role"] == "user":
                st.markdown(f"**You:** {turn['content']}")
            else:
                st.markdown(f"**Agent:** {turn['content']}")

    if st.button("Export Report"):
        st.warning("Report export functionality coming soon!")

else:
    st.info("Please upload a contract to begin analysis.")