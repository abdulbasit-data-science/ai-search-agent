# AI Search Chatbot

A Streamlit-based chatbot that combines AI language models with search capabilities using Groq and Tavily Search.

## Features

- Interactive chat interface using Streamlit
- Integration with Groq's Gemma 2 9B model
- Real-time web search capabilities via Tavily Search
- Session-based chat history
- ReAct agent implementation for improved reasoning

## Project Structure

```
ai-search-chatbot/
├── .env                    # Environment variables configuration
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
└── app.py                # Main application file
```

## Prerequisites

- Python 3.8+
- Groq API key
- Tavily API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abdulbasit-data-science/ai-search-chatbot.git
cd ai-search-chatbot
```

2. Create a virtual environment using `uv`:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
uv pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## Dependencies

Create a `requirements.txt` file with the following dependencies:

```
streamlit
python-dotenv
langchain-community
langchain-groq
langgraph
```

## Usage

1. Activate your virtual environment:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to `http://localhost:8501`

## How It Works

The chatbot combines several key components:
- Streamlit for the web interface
- Groq's Gemma 2 9B model for natural language processing
- Tavily Search for real-time web search capabilities
- LangChain's ReAct agent for reasoning and response generation

The application maintains a session-based chat history and can perform web searches to provide up-to-date information in responses.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Groq for providing the language model API
- Tavily for the search API
- Streamlit for the web framework
- LangChain for the agent framework
