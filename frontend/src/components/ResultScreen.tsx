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
    <div className="screen-container">
      <h1>🍿 Your Perfect Flavor!</h1>
      {result ? (
        <div className="result-content">
          <div className="flavor-name">
            {result.flavor}
          </div>
          {result.description && (
            <div className="flavor-description">
              {result.description}
            </div>
          )}
          <p style={{ fontSize: '0.9rem', opacity: 0.7, marginTop: '1.5rem' }}>
            ⚡ Generated in {result.duration?.toFixed(2) || '?'} seconds
          </p>
        </div>
      ) : (
        <div className="result-content">
          <p>Oops! Something went wrong. No result found.</p>
        </div>
      )}
      <div className="button-group">
        <button className="btn btn-primary" onClick={handleStartOver}>
          🔄 Create Another
        </button>
      </div>
    </div>
  );
};

export default ResultScreen;
