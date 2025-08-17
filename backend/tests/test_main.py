import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, mock_open, MagicMock
from main import app, log_session


client = TestClient(app)


class TestAPI:
    def test_root_endpoint(self):
        """Test the root endpoint returns expected message."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Moocorn backend is running!"}

    @patch('main.analyze_image')
    @patch('main.generate_flavor_suggestion')
    @patch('main.aiofiles.open')
    @patch('main.log_session')
    def test_generate_popcorn_success(self, mock_log, mock_aiofiles, mock_llm, mock_analyze):
        """Test successful popcorn generation with mocked dependencies."""
        # Mock file operations
        mock_file = MagicMock()
        mock_aiofiles.return_value.__aenter__.return_value = mock_file
        
        # Mock image analysis
        mock_analyze.return_value = {
            "lightness": "bright",
            "dominant_colors": [[255, 0, 0]],
            "brightness": 150
        }
        
        # Mock LLM response
        mock_llm.return_value = {
            "flavor": "Spicy Paprika Dream",
            "description": "A fiery blend perfect for your sunny disposition!"
        }
        
        # Mock image file
        mock_image = MagicMock()
        mock_image.read.return_value = b"fake_image_data"
        
        response = client.post(
            "/generate_popcorn",
            data={"name": "TestUser", "mood": "happy"},
            files={"image": ("test.jpg", mock_image, "image/jpeg")}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Popcorn generated successfully!"
        assert data["flavor"] == "Spicy Paprika Dream"
        assert data["description"] == "A fiery blend perfect for your sunny disposition!"
        
        # Verify mocks were called
        mock_analyze.assert_called_once()
        mock_llm.assert_called_once()
        mock_log.assert_called_once()


class TestLogSession:
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.isfile')
    def test_log_session_new_file(self, mock_isfile, mock_file):
        """Test logging session data to a new CSV file."""
        mock_isfile.return_value = False  # File doesn't exist
        
        log_session("Alice", "excited", "test.jpg", "Spicy", "Delicious!")
        
        # Verify file was opened for append
        mock_file.assert_called_once_with("data/sessions.csv", 'a', newline='')
        
        # Verify write operations (header + data row)
        handle = mock_file.return_value
        assert handle.write.call_count >= 2  # At least header and data