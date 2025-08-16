import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { generatePopcorn } from '../utils/api';

const ProgressScreen: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { name, mood, image } = location.state || {};

  useEffect(() => {
    const getPopcornFlavor = async () => {
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
    <div>
      <h1>Generating your popcorn flavor...</h1>
      {/* You can add a loading spinner here */}
    </div>
  );
};

export default ProgressScreen;
