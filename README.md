****AI Chatbot with Memory (LangChain Integration)****
->    This project is a conversational AI system that retrieves content from the internet, processes it, and generates responses using a large language model (LLM). The system features memory, allowing the chatbot to remember past conversations and provide contextual, fluent responses.
->    The backend utilizes FastAPI and LangChain for conversation memory and response generation. The frontend is built with React.js, providing an interactive user interface for inputting queries and displaying the AI-generated responses.

**Table of Contents**

    1.Project Overview
    2.Tech Stack
    3.Installation Instructions
    4.Backend Setup
    5.Frontend Setup
    6.Usage
    7.Folder Structure


**Project Overview**
->    This system consists of two main components:

->    Backend: A FastAPI service that interacts with the LangChain library to process user queries, retrieve relevant content from the web, and generate responses using a large language model. The backend also includes memory to make the conversation flow naturally.

->   Frontend: A React-based interface where users can input their queries and view the chatbot’s responses. The UI also displays the entire conversation history, allowing users to see context as the conversation progresses.

**Tech Stack**

Backend:
    FastAPI
    LangChain
    OpenAI API
    BeautifulSoup (for web scraping)
    Python-dotenv (for managing environment variables)

Frontend:
        React.js
        Axios (for API requests)

Other:
    Uvicorn (for running FastAPI)


**Installation Instructions**

Prerequisites
    Python 3.x (for the backend)
    Node.js (for the frontend)
    OpenAI API key (for LLM)

**Setting Up the Backend**

    1. Clone the repository:

        git clone https://github.com/your-username/ai-chatbot-with-memory.git
        cd ai-chatbot-with-memory

    2. Create a virtual environment for the backend:

        python -m venv venv
    
    3. Activate the virtual environment:

        venv\Scripts\activate

    4. Install backend dependencies:

        pip install -r backend/requirements.txt

    5. Set up your environment variables:

        OPENAI_API_KEY=your_openai_api_key_here

    6. Run the backend:

        uvicorn backend.app:app --reload

The backend should now be running at http://localhost:8000.

**Setting Up the Frontend**

    1. Change to the frontend directory:

        cd frontend

    2. Install frontend dependencies:

        npm install

    3. Start the frontend development server:

        npm start

The frontend should now be running at http://localhost:3000.

**Usage**

    1.Open your web browser and navigate to http://localhost:3000.
    2.You’ll be presented with a simple interface where you can input your query in a text box.
    3.After submitting a query, the backend will:
        Retrieve relevant web content based on your query.
        Process the content to extract the most meaningful text.
        Use the LLM (via LangChain) to generate a response, taking into account past conversations (memory).
    4.The response will be displayed in the UI, and the conversation history will be shown below.
    5.You can keep interacting with the chatbot, and it will remember previous messages.
    Contributing


**Folder Structure**

project
│
├── backend
│   ├── app.py                    # Main backend API (with memory)
│   ├── text_processing.py         # Text processing module
│   ├── content_retrieval.py       # Content retrieval module
│   ├── llm_integration.py         # LLM interaction module (with LangChain)
│   └── requirements.txt           # Dependencies
│
├── frontend
│   ├── public
│   ├── src
│   │   ├── App.js                 # Main app component
│   │   ├── components
│   │   │   ├── QueryForm.js       # Query input form
│   │   │   └── ResponseDisplay.js # Displays LLM response
│   │   └── services
│   │       └── apiService.js      # API service for backend requests
│   └── package.json               # Frontend dependencies
│
├── .env                           # Environment variables (API keys, etc.)
└── README.md 