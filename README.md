# 🤖 AI Search Chatbot  
A conversational AI chatbot with integrated web search, built using **Streamlit, LangChain, LangGraph, and Tavily API**.

## 🌟 Features  
- **Conversational AI** powered by Groq’s `gemma2-9b-it` model.  
- **Web Search Integration** using Tavily API.  
- **Memory** to maintain chat history in Streamlit.  
- **User-Friendly Interface** with interactive chat experience.  

## 🛠️ Technologies Used  
- **Python**  
- **Streamlit** (for UI)  
- **LangChain** & **LangGraph** (for agent behavior)  
- **Tavily API** (for web search)  
- **Groq AI** (for LLM-powered responses)  


## 🚀 Installation  
### **1️⃣ Clone the repository**  
```bash
git clone https://github.com/abdulbasit-data-science/ai-search-chatbot.git
cd ai-search-chatbot

2️⃣ Set up a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set up API keys
Create a .env file in the project root and add:

env
Copy
Edit
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
5️⃣ Run the chatbot
bash
Copy
Edit
streamlit run app.py
📸 Screenshots (Optional)
If you have a UI screenshot, add it inside the assets/ folder and reference it like this:

md
Copy
Edit
![Chatbot UI](assets/chatbot-ui.png)
🤝 Contributing
Contributions are welcome! If you'd like to improve this chatbot, feel free to submit a pull request.

📜 License
This project is licensed under the MIT License.

⭐ Show Some Support!
If you like this project, don't forget to star ⭐ this repository on GitHub! 🚀


