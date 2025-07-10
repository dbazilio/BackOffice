


import './App.css';
import React from 'react';
import Chatbot from './Chatbot';
import './Chatbot.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div style={{ width: '100%', maxWidth: 600, margin: '32px auto 0 auto' }}>
          <Chatbot />
        </div>
      </header>
    </div>
  );
}

export default App;
