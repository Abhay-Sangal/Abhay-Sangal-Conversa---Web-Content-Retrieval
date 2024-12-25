// frontend/src/App.js
import React, { useState } from "react";
import QueryForm from "./components/QueryForm";
import ResponseDisplay from "./components/ResponseDisplay";

function App() {
  const [response, setResponse] = useState("");
  const [history, setHistory] = useState([]);

  return (
    <div>
      <h1>AI Response Generator</h1>
      <QueryForm setResponse={setResponse} history={history} setHistory={setHistory} />
      <ResponseDisplay history={history} />
    </div>
  );
}

export default App;
