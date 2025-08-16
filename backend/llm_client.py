import openai
import os

# It's recommended to set these as environment variables
# For LocalAI, the API key can be any string.
LOCALAI_API_KEY = os.getenv("LOCALAI_API_KEY", "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
LOCALAI_BASE_URL = os.getenv("LOCALAI_BASE_URL", "http://localhost:8080/v1")

client = openai.OpenAI(
    api_key=LOCALAI_API_KEY,
    base_url=LOCALAI_BASE_URL,
)

def read_flavors() -> list[str]:
    """Reads the list of available flavors from the flavors.txt file."""
    try:
        with open("data/flavors.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def generate_flavor_suggestion(name: str, mood: str, image_analysis: dict) -> dict:
    """
    Generates a popcorn flavor suggestion using the LLM.
    """
    flavors = read_flavors()
    if not flavors:
        return {"error": "Flavor list is empty or not found."}

    # Construct the prompt
    prompt = f"""You are an intelligent popcorn flavoring machine at Burning Man.
Given the user's name: {name},
mood: {mood},
image lightness: {image_analysis.get('lightness', 'unknown')},
dominant colors: {image_analysis.get('dominant_colors', 'unknown')},

Generate them a popcorn flavor (a combination of seasonings) and an accompanying short description with a witty and whimsical tone.

These are the list of flavors available: {', '.join(flavors)}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Replace with your LocalAI model name
            messages=[
                {"role": "system", "content": "You are a whimsical popcorn flavor generator."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
        )
        suggestion = response.choices[0].message.content
        # A simple way to parse the output, you might need to adjust this
        parts = suggestion.split("\n\n")
        flavor = parts[0].replace("Flavor:", "").strip()
        description = parts[1].replace("Description:", "").strip() if len(parts) > 1 else ""

        return {"flavor": flavor, "description": description}

    except Exception as e:
        return {"error": str(e)}
