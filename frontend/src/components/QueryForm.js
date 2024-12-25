// frontend/src/components/QueryForm.js
import React, { useState } from "react";
import axios from "axios";

function QueryForm({ setResponse, history, setHistory }) {
  const [query, setQuery] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send query to backend
      const res = await axios.post("http://localhost:8000/generate_response/", { query });
      
      // Add user query and response to the conversation history
      const newHistory = [...history, { user: query, bot: res.data.response }];
      setHistory(newHistory);
      setQuery("");  // Clear input field
    } catch (error) {
      console.error("Error retrieving response:", error);
      setResponse("Error retrieving response.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask me anything..." />
      <button type="submit">Submit</button>
    </form>
  );
}

export default QueryForm;
