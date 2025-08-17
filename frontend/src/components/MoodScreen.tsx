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

  const moodOptions = [
    'Happy', 'Excited', 'Calm', 'Adventurous', 
    'Nostalgic', 'Creative', 'Energetic', 'Contemplative'
  ];

  const handleMoodSelect = (selectedMood: string) => {
    setMood(selectedMood);
    navigate('/camera', { state: { name, mood: selectedMood } });
  };

  return (
    <div className="screen-container">
      <h1>How are you feeling, {name}?</h1>
      <p>Choose a mood or describe your own</p>
      
      <div className="mood-buttons">
        {moodOptions.map((moodOption) => (
          <button
            key={moodOption}
            className="btn btn-mood"
            onClick={() => handleMoodSelect(moodOption)}
          >
            {moodOption}
          </button>
        ))}
      </div>

      <input
        type="text"
        placeholder="Or enter your own mood..."
        value={mood}
        onChange={(e) => setMood(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && handleNext()}
      />
      
      <div className="button-group">
        <button className="btn btn-primary" onClick={handleNext} disabled={!mood.trim()}>
          Next
        </button>
        <button className="btn btn-secondary" onClick={handleCancel}>
          Cancel
        </button>
      </div>
    </div>
  );
};

export default MoodScreen;
