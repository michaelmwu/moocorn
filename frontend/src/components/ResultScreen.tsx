import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const ResultScreen: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { result } = location.state || {};

  const handleStartOver = () => {
    navigate('/');
  };

  return (
    <div>
      <h1>Your Popcorn Flavor</h1>
      {result ? (
        <>
          <h2>Flavor: {result.flavor}</h2>
          <p>Description: {result.description}</p>
        </>
      ) : (
        <p>No result found.</p>
      )}
      <button onClick={handleStartOver}>Start Over</button>
    </div>
  );
};

export default ResultScreen;
