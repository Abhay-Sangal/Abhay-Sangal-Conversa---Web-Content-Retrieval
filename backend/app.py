# backend/app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from content_retrieval import fetch_web_content
from text_processing import process_text
from llm_integration import generate_llm_response
import os
from dotenv import load_dotenv
import traceback

load_dotenv()  # Load environment variables from .env file

openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the key is being loaded correctly
print(openai_api_key)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend API is up and running!"}

class QueryRequest(BaseModel):
    query: str

@app.post("/generate_response/")
async def generate_response(request: QueryRequest):
    try:
        # Step 1: Retrieve web content
        print(f"Fetching web content for query: {request.query}")
        web_content = fetch_web_content(request.query)
        
        # Step 2: Process retrieved content
        print("Processing the retrieved content...")
        processed_text = process_text(web_content)
        
        # Step 3: Generate LLM response
        print("Generating response using LLM...")
        response = generate_llm_response(request.query, processed_text)
        
        return {"response": response}
    
    except Exception as e:
        # Log the full stack trace for debugging
        error_message = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)  # Print error message for visibility
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")


