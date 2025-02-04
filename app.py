import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage

# Load environment variables
load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

def main():
    st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
    st.title("🤖 AI Chatbot with Search")
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Setup tools and model
    search = TavilySearchResults(max_results=2)
    tools = [search]
    
    model = ChatGroq(
        model="deepseek-r1-distill-llama-70b", 
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Create agent with proper configuration
    agent = create_react_agent(
        model,
        tools,
        
    )
    
    # User input
    user_input = st.chat_input("Ask me anything...")
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Create message list for agent
        messages = [
            HumanMessage(content=user_input)
        ]
        
        # Get agent response
        response = agent.invoke({
            "messages": messages,
            "structured_response": False
        })
        
        # Extract assistant message from response
        if isinstance(response, dict) and "messages" in response:
            assistant_message = response["messages"][-1]
            assistant_response = assistant_message.content
        else:
            assistant_response = str(response)
        
        # Display and store assistant response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_response
        })

if __name__ == "__main__":
    main()
