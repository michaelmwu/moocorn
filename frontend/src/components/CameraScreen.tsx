import React, { useRef, useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const CameraScreen: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { name, mood } = location.state || {};
  const videoRef = useRef<HTMLVideoElement>(null);
  const [stream, setStream] = useState<MediaStream | null>(null);

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
  }, [stream]);

  const handleTakePicture = () => {
    if (videoRef.current) {
      const canvas = document.createElement('canvas');
      canvas.width = videoRef.current.videoWidth;
      canvas.height = videoRef.current.videoHeight;
      const context = canvas.getContext('2d');
      if (context) {
        context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
        canvas.toBlob((blob) => {
          if (blob) {
            const imageFile = new File([blob], "capture.jpg", { type: "image/jpeg" });
            navigate('/progress', { state: { name, mood, image: imageFile } });
          }
        }, 'image/jpeg');
      }
    }
  };

  const handleCancel = () => {
    navigate('/');
  };

  return (
    <div>
      <h1>Camera</h1>
      <video ref={videoRef} autoPlay style={{ width: '100%', height: '400px', backgroundColor: 'black' }} />
      <button onClick={handleTakePicture}>Take Picture</button>
      <button onClick={handleCancel}>Cancel</button>
    </div>
  );
};

export default CameraScreen;
