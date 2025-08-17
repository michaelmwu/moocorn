import React, { useEffect, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { generatePopcorn } from '../utils/api';

const ProgressScreen: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { name, mood, image } = location.state || {};
  const hasCalledRef = useRef(false);

  useEffect(() => {
    const getPopcornFlavor = async () => {
      if (hasCalledRef.current) return; // Prevent duplicate calls
      hasCalledRef.current = true;
      
      try {
        const result = await generatePopcorn(name, mood, image);
        navigate('/result', { state: { result } });
      } catch (error) {
        console.error('Error generating popcorn:', error);
        // Handle error, maybe navigate to an error screen
        navigate('/'); // For now, just go back to the start
      }
    };

    if (name && mood && image) {
      getPopcornFlavor();
    }
  }, [name, mood, image, navigate]);

  return (
    <div className="screen-container">
      <h1>Crafting Your Flavor...</h1>
      <p>Analyzing your {mood} mood and photo to create the perfect popcorn experience for you, {name}!</p>
      <div className="spinner"></div>
      <p style={{ fontSize: '0.9rem', opacity: 0.8, marginTop: '2rem' }}>
        ✨ This may take a few moments
      </p>
    </div>
  );
};

export default ProgressScreen;
