
# 🧠 Real-time Indian News AI Chatbot

> A full-stack AI-powered application that delivers real-time answers to user queries based on the latest Indian news — using Pathway, Ollama, and Streamlit. Supports topic alerts, domain-based filtering, and a modern chat interface.

---

## 📌 Features

✅ Real-time Retrieval-Augmented Generation (RAG)  
✅ Indian news via Exa API  
✅ Ollama-powered local LLM (LLaMA3)  
✅ User-friendly AI chatbot interface (Streamlit)  
✅ Topic-based notification alerts  
✅ Domain-based filtering (sports, politics, tech, etc.)

---

## 🧱 Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Backend    | Python + FastAPI + Pathway |
| Embeddings | sentence-transformers (local) |
| LLM        | Ollama (`llama3`, `mistral`, etc.) |
| Frontend   | Streamlit (chat-style UI) |
| Data Feed  | Exa API (for latest Indian news) |

---

## 📦 Clone & Setup

### 🔧 Prerequisites

- WSL 2 (Linux Subsystem on Windows) or native Linux/macOS
- Python 3.10+
- [Ollama installed](https://ollama.com)
- `llama3` or similar model pulled via Ollama

---

### 📁 Clone the Repository

```bash
git clone https://github.com/your-username/realtime-rag-bot.git
cd realtime-rag-bot
```

---

## ⚙️ Backend Setup (WSL or Linux)

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install backend dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 📄 Create `.env` file

```env
EXA_API_KEY=your_exa_api_key_here
```

> Get your key from: [https://exa.ai](https://exa.ai)

---

### ▶️ Run Ollama

Make sure Ollama is installed and running:

```bash
ollama run llama3
```

> First time? This will download the model (~4–7GB)

---

### ▶️ Run FastAPI Backend

```bash
uvicorn backend.api.app:app --reload --port 8000
```

Open: [http://localhost:8000/docs](http://localhost:8000/docs)  
to test `/ask` and `/subscribe` endpoints.

---

## 💬 Frontend (Streamlit)

In a new terminal:

```bash
cd frontend
source ../.venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open in browser: [http://localhost:8501](http://localhost:8501)

---

## 💻 Usage

### 🧠 Ask AI Questions

- Enter your question (e.g., “What’s new in Indian elections?”)
- Select a domain (e.g., politics, sports)
- Get an answer generated using real-time indexed news

### 🔔 Subscribe to Topic Alerts

- Enter a keyword (e.g., “cricket”)
- Get notified (in logs or UI) when relevant news is ingested

---

## 🧪 Testing the Flow

1. Run Ollama
2. Start backend
3. Run Streamlit
4. Subscribe to a topic (e.g., "ipl")
5. Ask a domain-specific question (e.g., "Any updates in IPL?")

---

## 📁 Project Structure

```
realtime-rag-bot/
│
├── backend/
│   ├── ingestion/             # Exa news fetch + stream
│   ├── pathway_pipeline/      # Real-time ETL using Pathway
│   ├── retrieval/             # Vector search + prompt creation
│   ├── llm/                   # Ollama LLM client
│   ├── api/                   # FastAPI endpoints
│   └── config/                # Subscriptions store
│
├── frontend/                  # Streamlit chat UI
│   ├── app.py
│   └── requirements.txt
│
├── .env                       # EXA API key
├── requirements.txt           # Backend deps
└── README.md
```

---

## 🔧 Dev Tips

- Customize LLM: Change `MODEL_NAME` in `ollama_client.py`
- Add more domains: Extend `domain` choices in Streamlit
- Add email/Slack alerts: Replace `print()` with webhook/email logic
- For production: Add Docker support or deploy on Hugging Face Spaces

---

## 🤝 Credits

Built for the **Pathway Real-time RAG Playground Hackathon**  
Tech powered by:
- [Pathway](https://pathway.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [Exa API](https://exa.ai/)

---

## 🪪 License

MIT License. See `LICENSE` file.
