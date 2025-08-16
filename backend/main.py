
import csv
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from models import GeneratePopcornRequest
from image_processor import analyze_image
from llm_client import generate_flavor_suggestion
import datetime
import aiofiles
import os

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Default React dev server port
    "http://localhost:1234",  # Example port for Electron
    "app://.",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure data directories exist
os.makedirs("data/images", exist_ok=True)

CSV_FILE = "data/sessions.csv"

def log_session(name: str, mood: str, image_filename: str, flavor: str, description: str):
    """Appends session data to the CSV file."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'name', 'mood', 'image_filename', 'flavor', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': datetime.datetime.now().isoformat(),
            'name': name,
            'mood': mood,
            'image_filename': image_filename,
            'flavor': flavor,
            'description': description,
        })

@app.get("/")
def read_root():
    return {"message": "Moocorn backend is running!"}


@app.post("/generate_popcorn")
async def generate_popcorn(
    name: str = Form(...),
    mood: str = Form(...),
    image: UploadFile = File(...)
):
    start_time = datetime.datetime.now()
    image_filename = f"{start_time.strftime('%Y%m%d_%H%M%S')}_{name}.jpg"
    image_path = f"data/images/{image_filename}"

    # Save the image
    async with aiofiles.open(image_path, 'wb') as out_file:
        content = await image.read()
        await out_file.write(content)

    # Analyze the image
    analysis_results = analyze_image(image_path)
    if analysis_results.get("error"):
        return {"error": f"Image analysis failed: {analysis_results['error']}"}

    # Generate flavor suggestion
    suggestion = generate_flavor_suggestion(name, mood, analysis_results)
    if suggestion.get("error"):
        return {"error": f"LLM request failed: {suggestion['error']}"}

    # Log the session
    log_session(
        name=name,
        mood=mood,
        image_filename=image_filename,
        flavor=suggestion.get("flavor", ""),
        description=suggestion.get("description", "")
    )

    return {
        "message": "Popcorn generated successfully!",
        "flavor": suggestion.get("flavor"),
        "description": suggestion.get("description"),
        "image_analysis": analysis_results
    }

