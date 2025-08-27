import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const ResultScreen: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { result } = location.state || {};

  useEffect(() => {
    if (!result) {
      navigate('/', { replace: true });
    }
  }, [result, navigate]);

  const handleStartOver = () => {
    navigate('/');
  };

  var raw_flavor = result.flavor.trim();
  var newline = raw_flavor.search("\n");

  console.log("newline: " + newline);

  var flavor = newline > 0 ? raw_flavor.substring(0, newline) : raw_flavor;
  var description = newline > 0 ? raw_flavor.substring(newline+1) : "";

  console.log("raw_flavor: " + raw_flavor);
  console.log("flavor: " + flavor);
  console.log("description: " + description);

  return (
    <div className="screen-container">
      <h1>🍿 Your Perfect Flavor!</h1>
      {result ? (
        <div className="result-content">
          <div className="flavor-name">
            {flavor}
          </div>
          <div className="flavor-description">
            {description}
          </div>
          <p style={{ fontSize: '1.2rem', marginTop: '1.5rem' }}>
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
