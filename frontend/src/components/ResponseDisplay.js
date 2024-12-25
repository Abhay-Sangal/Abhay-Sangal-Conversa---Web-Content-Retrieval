// frontend/src/components/ResponseDisplay.js
import React from "react";

function ResponseDisplay({ history }) {
  return (
    <div>
      <h2>Conversation:</h2>
      {history.map((entry, index) => (
        <div key={index}>
          <p><strong>You:</strong> {entry.user}</p>
          <p><strong>Bot:</strong> {entry.bot}</p>
        </div>
      ))}
    </div>
  );
}

export default ResponseDisplay;

