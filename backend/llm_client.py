import openai
from settings import settings

# Configure the OpenAI client based on settings
if settings.llm_provider == "openrouter":
    base_url = "https://openrouter.ai/api/v1"
else: # localai or openai
    base_url = settings.llm_base_url

client = openai.OpenAI(
    api_key=settings.llm_api_key or "ollama",  # Ollama doesn't need a real API key
    base_url=base_url,
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
    prompt = f"""
Given the user's name: {name},
mood: {mood},
image lightness: {image_analysis.get('lightness', 'unknown')},
dominant colors: {', '.join(image_analysis.get('dominant_color_names', ['unknown']))},

Generate them a popcorn flavor (a combination of seasonings) with an accompanying short (1-2 paragraphs, not too long please!) description with a witty and whimsical tone.

These are the list of flavors available: {', '.join(flavors)}
"""

    try:
        response = client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": "You are an whimiscal popcorn flavoring machine at Burning Man."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
        )
        flavor_suggestion = response.choices[0].message.content
        return {"flavor": flavor_suggestion}

    except Exception as e:
        return {"error": str(e)}
