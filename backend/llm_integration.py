# backend/llm_integration.py

import os
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize LangChain LLM with conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = OpenAI(api_key=openai_api_key, model="text-davinci-003", temperature=0.7)

# Create a conversational chain using the LLM and memory
conversation_chain = ConversationChain(llm=llm, memory=memory)

def generate_llm_response(query, content):
    """
    Generates a response using the LLM, leveraging conversational memory for context.
    """
    prompt = f"User Query: {query}\n\nRelated Content: {content}\n\nResponse:"
    response = conversation_chain.predict(input=prompt)
    
    return response
