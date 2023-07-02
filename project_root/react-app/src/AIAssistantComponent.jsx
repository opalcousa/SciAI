import React, { useState } from 'react';
import axios from 'axios';

const AIAssistantComponent = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const handleChange = (event) => {
        setMessage(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post('/api/ai_assistant/', { message: message })
            .then(res => {
                setResponse(res.data.response);
            })
            .catch(err => {
                console.error(err);
            });
    }

    return (
        <div>
            <h2>AI Assistant</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Ask the AI Assistant:
                    <input type="text" value={message} onChange={handleChange} />
                </label>
                <input type="submit" value="Ask" />
            </form>
            <p>{response}</p>
        </div>
    );
}

export default AIAssistantComponent;