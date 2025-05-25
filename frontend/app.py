import streamlit as st
import requests

st.set_page_config(page_title="🧠 Real-time News AI", layout="centered")

API_BASE = "http://localhost:8000"

# --- App Title ---
st.markdown("""
    <h1 style="text-align: center;">📰 Real-time Indian News Chatbot</h1>
    <p style="text-align: center; font-size: 18px;">Powered by Pathway, Ollama, and RAG 🔁</p>
""", unsafe_allow_html=True)

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat Input Panel ---
with st.container():
    with st.form("chat_form", clear_on_submit=True):
        cols = st.columns([3, 1])
        question = cols[0].text_input("Ask something...")
        domain = cols[1].selectbox("Domain", ["general", "politics", "sports", "technology", "economy"])
        submitted = st.form_submit_button("💬 Ask")

# --- Send to Backend ---
if submitted and question.strip():
    st.session_state.messages.append({"role": "user", "text": question})
    with st.spinner("Fetching answer..."):
        try:
            res = requests.post(f"{API_BASE}/ask", json={"question": question, "domain": domain})
            if res.status_code == 200:
                answer = res.json().get("answer", "No answer received.")
            else:
                answer = "Error: Could not get a response."
        except Exception as e:
            answer = f"Error: {str(e)}"
    st.session_state.messages.append({"role": "bot", "text": answer})

# --- Chat Display ---
st.markdown("---")
for msg in st.session_state.messages[::-1]:
    is_user = msg["role"] == "user"
    box_color = "#e0f7fa" if is_user else "#f1f8e9"
    align = "flex-end" if is_user else "flex-start"
    st.markdown(f"""
    <div style="display: flex; justify-content: {align}; padding: 4px;">
        <div style="background-color: {box_color}; padding: 10px 15px; border-radius: 15px; max-width: 80%;">
            {msg["text"]}
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Topic Subscription ---
with st.expander("🔔 Subscribe to topic alerts"):
    with st.form("subscribe_form", clear_on_submit=True):
        topic = st.text_input("Subscribe to a topic (e.g., cricket, elections)")
        sub_btn = st.form_submit_button("🔔 Subscribe")
        if sub_btn and topic.strip():
            try:
                res = requests.post(f"{API_BASE}/subscribe", json={"question": topic})
                if res.status_code == 200:
                    st.success(f"Subscribed to '{topic.strip()}'")
                else:
                    st.error("Failed to subscribe.")
            except Exception as e:
                st.error(str(e))
