import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const ErrorScreen: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { error } = location.state || {};

  useEffect(() => {
    if (!error) {
      navigate('/', { replace: true });
    }
  }, [error, navigate]);

  const handleGoBack = () => {
    navigate('/');
  };

  const getErrorMessage = (error: any): string => {
    if (typeof error === 'string') return error;
    if (error?.message) return error.message;
    if (error instanceof Error) return error.message;
    return 'An unexpected error occurred';
  };

  const getErrorDetails = (error: any): string => {
    // Network errors
    if (error?.message?.includes('fetch')) {
      return 'Unable to connect to the server. Please check your internet connection or try again later.';
    }
    
    // Timeout errors
    if (error?.message?.includes('timeout')) {
      return 'The request took too long to complete. The server might be busy - please try again in a moment.';
    }

    // API errors
    if (error?.status) {
      switch (error.status) {
        case 500:
          return 'The server encountered an internal error. Our popcorn machine might be having a moment!';
        case 503:
          return 'The service is temporarily unavailable. Please try again shortly.';
        case 404:
          return 'The requested service could not be found.';
        default:
          return `Server returned error ${error.status}. Please try again.`;
      }
    }

    return 'Something went wrong while crafting your popcorn flavor. Please try again.';
  };

  if (!error) return null;

  return (
    <div className="screen-container">
      <h1>🚫 Oops!</h1>
      <div className="result-content">
        <h2 style={{ color: '#ff6b6b', marginBottom: '1rem' }}>
          Something Went Wrong
        </h2>
        <p style={{ marginBottom: '1.5rem', fontSize: '1.1rem' }}>
          {getErrorDetails(error)}
        </p>
        <details style={{ 
          background: 'rgba(255, 255, 255, 0.1)', 
          padding: '1rem', 
          borderRadius: '8px',
          marginBottom: '1.5rem',
          fontSize: '0.9rem'
        }}>
          <summary style={{ cursor: 'pointer', fontWeight: 'bold' }}>
            Technical Details
          </summary>
          <p style={{ marginTop: '0.5rem', fontFamily: 'monospace' }}>
            {getErrorMessage(error)}
          </p>
        </details>
      </div>
      <div className="button-group">
        <button className="btn btn-primary" onClick={handleGoBack}>
          🏠 Start Over
        </button>
      </div>
    </div>
  );
};

export default ErrorScreen;