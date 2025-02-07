# 🚀 AI Search Agent

A **Streamlit-powered AI agent** that integrates **Groq AI models** with **real-time web search** using Tavily Search! 🌍🤖

---

## ✨ Features

✅ **Interactive Chat Interface** powered by Streamlit  
✅ **Deepseek-r1 Integration** for natural language understanding  
✅ **Real-time Web Search** with Tavily Search API  
✅ **Session-based Chat History** for seamless conversations  
✅ **ReAct Agent Implementation** for enhanced reasoning  

---

## 📁 Project Structure

```bash
ai-search-agent/
├── .env                # Environment variables configuration
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
├── requirements.txt   # Project dependencies
└── app.py            # Main application file
```

---

## ⚡ Prerequisites

Before running the project, ensure you have:
- 🐍 **Python 3.8+** installed
- 🔑 **Groq API Key** (for AI model access)
- 🔑 **Tavily API Key** (for web search capabilities)

---

## 🔧 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abdulbasit-data-science/ai-search-agent.git
cd ai-search-chatbot
```

### 2️⃣ Set Up a Virtual Environment
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
uv pip install -r requirements.txt
```

### 4️⃣ Configure API Keys
Create a `.env` file in the root directory and add:
```ini
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 📌 Dependencies
Ensure you have the following dependencies installed:
```txt
streamlit
python-dotenv
langchain-community
langchain-groq
langgraph
```

---

## 🚀 Usage

### 1️⃣ Activate Virtual Environment
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

### 3️⃣ Open the App
Navigate to [`http://localhost:8501`](http://localhost:8501) in your web browser. 🌐

---

## 🛠️ How It Works

The AI Search Agent integrates:
- 🖥 **Streamlit** → for an interactive web interface
- 🤖 **Deepseek-r1** → for AI-based responses
- 🔎 **Tavily Search** → for real-time web searches
- 🧠 **LangChain's ReAct Agent** → for better reasoning and response generation

It maintains **session-based chat history** and fetches **real-time information** to enhance responses! 🚀

---

## 🤝 Contributing

Want to make this project even better? Follow these steps:
1. **Fork the repository** 🍴
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add some amazing feature'`)
4. **Push to your branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request** 📩

---

## 🙌 Acknowledgments

💡 **Thanks to these amazing tools & services:**
- 🏆 **Groq** → for AI model API
- 🔍 **Tavily** → for search API
- 🎨 **Streamlit** → for the web framework
- 🔗 **LangChain** → for the agent framework

---

### 📢 Star ⭐ the repo if you find it useful! Happy coding! 🚀

