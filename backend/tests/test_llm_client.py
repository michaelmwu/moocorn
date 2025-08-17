import pytest
from unittest.mock import patch, mock_open, MagicMock
from llm_client import read_flavors, generate_flavor_suggestion


class TestReadFlavors:
    @patch('builtins.open', new_callable=mock_open, read_data='paprika\nwhite pepper\ngarlic powder\n')
    def test_read_flavors_success(self, mock_file):
        """Test reading flavors from file successfully."""
        flavors = read_flavors()
        
        assert flavors == ['paprika', 'white pepper', 'garlic powder']
        mock_file.assert_called_once_with("data/flavors.txt", "r")

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_flavors_file_not_found(self, mock_file):
        """Test reading flavors when file doesn't exist."""
        flavors = read_flavors()
        
        assert flavors == []


class TestGenerateFlavorSuggestion:
    @patch('llm_client.read_flavors')
    def test_generate_flavor_no_flavors(self, mock_read_flavors):
        """Test flavor generation when no flavors are available."""
        mock_read_flavors.return_value = []
        
        result = generate_flavor_suggestion("Alice", "happy", {"lightness": "bright"})
        
        assert "error" in result
        assert result["error"] == "Flavor list is empty or not found."

    @patch('llm_client.read_flavors')
    @patch('llm_client.client.chat.completions.create')
    def test_generate_flavor_success(self, mock_create, mock_read_flavors):
        """Test successful flavor generation."""
        # Mock flavors
        mock_read_flavors.return_value = ['paprika', 'garlic', 'pepper']
        
        # Mock LLM response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Spicy Paprika Delight\n\nA perfect blend for your sunny mood!"
        mock_create.return_value = mock_response
        
        result = generate_flavor_suggestion(
            "Alice", 
            "happy", 
            {"lightness": "bright", "dominant_colors": [[255, 0, 0]]}
        )
        
        assert "error" not in result
        assert result["flavor"] == "Spicy Paprika Delight"
        assert result["description"] == "A perfect blend for your sunny mood!"
        
        # Verify LLM was called with correct parameters
        mock_create.assert_called_once()

    @patch('llm_client.read_flavors')
    @patch('llm_client.client.chat.completions.create')
    def test_generate_flavor_llm_error(self, mock_create, mock_read_flavors):
        """Test flavor generation when LLM call fails."""
        mock_read_flavors.return_value = ['paprika']
        mock_create.side_effect = Exception("LLM connection failed")
        
        result = generate_flavor_suggestion("Alice", "happy", {"lightness": "bright"})
        
        assert "error" in result
        assert "LLM connection failed" in result["error"]