import pytest
from unittest.mock import patch, MagicMock
from image_processor import analyze_image


class TestAnalyzeImage:
    @patch('image_processor.cv2.imread')
    def test_analyze_image_returns_expected_structure(self, mock_imread):
        """Test that analyze_image returns the expected data structure without actual image processing."""
        # Mock cv2.imread to return None (simulating file not found)
        mock_imread.return_value = None
        
        result = analyze_image("test.jpg")
        
        # Should return error when image can't be read
        assert "error" in result
        assert result["error"] == "Could not read image"
        
        # Verify cv2.imread was called with the correct path
        mock_imread.assert_called_once_with("test.jpg")

    def test_analyze_image_with_invalid_path(self):
        """Test analyze_image with an obviously invalid path - this will be fast."""
        result = analyze_image("")
        
        # Should return error for empty path
        assert "error" in result