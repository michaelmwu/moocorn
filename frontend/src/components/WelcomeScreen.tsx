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
    <div>
      <h1>Welcome to Moocorn, the intelligent popcorn machine.</h1>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={handleNext}>Next</button>
    </div>
  );
};

export default WelcomeScreen;
