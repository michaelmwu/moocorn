import React, { useRef, useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const CameraScreen: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { name, mood } = location.state || {};
  const videoRef = useRef<HTMLVideoElement>(null);
  const [stream, setStream] = useState<MediaStream | null>(null);

  useEffect(() => {
    if (!name || !mood) {
      navigate('/', { replace: true });
      return;
    }
  }, [name, mood, navigate]);

  useEffect(() => {
    const getCamera = async () => {
      try {
        const mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
        setStream(mediaStream);
        if (videoRef.current) {
          videoRef.current.srcObject = mediaStream;
        }
      } catch (err) {
        console.error("Error accessing camera: ", err);
      }
    };

    getCamera();

    return () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
    };
  }, []);

  const handleTakePicture = () => {
    if (videoRef.current) {
      const canvas = document.createElement('canvas');
      // Get camera resolution from environment variables
      const maxWidth = parseInt(import.meta.env.VITE_CAMERA_MAX_WIDTH) || 1024;
      const maxHeight = parseInt(import.meta.env.VITE_CAMERA_MAX_HEIGHT) || 768;
      const aspectRatio = videoRef.current.videoWidth / videoRef.current.videoHeight;
      
      if (aspectRatio > maxWidth / maxHeight) {
        canvas.width = maxWidth;
        canvas.height = maxWidth / aspectRatio;
      } else {
        canvas.width = maxHeight * aspectRatio;
        canvas.height = maxHeight;
      }
      
      const context = canvas.getContext('2d');
      if (context) {
        context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
        canvas.toBlob((blob) => {
          if (blob) {
            const imageFile = new File([blob], "capture.jpg", { type: "image/jpeg" });
            navigate('/progress', { state: { name, mood, image: imageFile } });
          }
        }, 'image/jpeg', 0.8); // Reduce quality to 80% for smaller file size
      }
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  const handleSkipPhoto = () => {
    navigate('/progress', { state: { name, mood, image: null } });
  };

  return (
    <div className="screen-container">
      <h1>Strike a Pose!</h1>
      <p>Take a photo that captures your {mood} mood</p>
      <video 
        ref={videoRef} 
        autoPlay 
        style={{ 
          width: '100%', 
          maxWidth: '400px',
          height: 'auto',
          aspectRatio: '4/3',
          backgroundColor: 'black' 
        }} 
      />
      <div className="button-group">
        <button className="btn btn-primary" onClick={handleTakePicture}>
          📸 Capture
        </button>
        <button className="btn btn-secondary" onClick={handleSkipPhoto}>
          🕶️ Keep It Mysterious
        </button>
        <button className="btn btn-secondary" onClick={handleCancel}>
          Cancel
        </button>
      </div>
    </div>
  );
};

export default CameraScreen;
