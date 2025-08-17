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
    <div style={{ textAlign: 'center', paddingTop: '50px' }}>
      <style>
        {`
          .spinner {
            border: 8px solid #f3f3f3; /* Light grey */
            border-top: 8px solid #3498db; /* Blue */
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 2s linear infinite;
            display: inline-block;
          }

          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
        `}
      </style>
      <h1>Generating your popcorn flavor...</h1>
      <div className="spinner"></div>
    </div>
  );
};

export default ProgressScreen;
