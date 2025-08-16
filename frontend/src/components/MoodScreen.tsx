import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const MoodScreen: React.FC = () => {
  const [mood, setMood] = useState('');
  const navigate = useNavigate();
  const location = useLocation();
  const name = location.state?.name || '';

  const handleNext = () => {
    if (mood.trim() !== '') {
      navigate('/camera', { state: { name, mood } });
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  return (
    <div>
      <h1>How are you feeling today, {name}?</h1>
      <input
        type="text"
        placeholder="Enter your mood"
        value={mood}
        onChange={(e) => setMood(e.target.value)}
      />
      <button onClick={handleNext}>Next</button>
      <button onClick={handleCancel}>Cancel</button>
    </div>
  );
};

export default MoodScreen;
