
import React, { useState } from 'react';
import './Chatbot.css';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = async (e) => {
    e.preventDefault();
    if (input.trim() === '') return;
    const userMsg = { text: input, from: 'user' };
    setMessages((msgs) => [...msgs, userMsg]);
    setLoading(true);
    try {
      const res = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
      if (res.ok) {
        const data = await res.json();
        setMessages((msgs) => [...msgs, { text: data.response, from: 'bot' }]);
      } else {
        setMessages((msgs) => [...msgs, { text: 'Estamos trabalhando para melhor atendê-los', from: 'bot' }]);
      }
    } catch (err) {
      setMessages((msgs) => [...msgs, { text: 'Estamos trabalhando para melhor atendê-los', from: 'bot' }]);
    }
    setInput('');
    setLoading(false);
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`chatbot-message chatbot-message-${msg.from}`}>
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className="chatbot-message chatbot-message-bot">Digitando...</div>
        )}
      </div>
      <form className="chatbot-input-area" onSubmit={handleSend}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Digite sua mensagem..."
          disabled={loading}
        />
        <button type="submit" disabled={loading}>Enviar</button>
      </form>
    </div>
  );
}

export default Chatbot;
