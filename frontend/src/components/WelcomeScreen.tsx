import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const WelcomeScreen: React.FC = () => {
  const [name, setName] = useState('');
  const navigate = useNavigate();

  const handleNext = () => {
    if (name.trim() !== '') {
      navigate('/mood', { state: { name } });
    }
  };

  return (
    <div className="screen-container">
      <h1>Welcome to Moocorn</h1>
      <p>The intelligent popcorn machine that creates flavors based on your mood.</p>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && handleNext()}
        autoFocus
      />
      <button className="btn btn-primary" onClick={handleNext} disabled={!name.trim()}>
        Get Started
      </button>
    </div>
  );
};

export default WelcomeScreen;
