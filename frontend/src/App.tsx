import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import WelcomeScreen from './components/WelcomeScreen';
import MoodScreen from './components/MoodScreen';
import CameraScreen from './components/CameraScreen';
import ProgressScreen from './components/ProgressScreen';
import ResultScreen from './components/ResultScreen';
import ErrorScreen from './components/ErrorScreen';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/mood" element={<MoodScreen />} />
        <Route path="/camera" element={<CameraScreen />} />
        <Route path="/progress" element={<ProgressScreen />} />
        <Route path="/result" element={<ResultScreen />} />
        <Route path="/error" element={<ErrorScreen />} />
      </Routes>
    </Router>
  );
}

export default App;