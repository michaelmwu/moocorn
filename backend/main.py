
import csv
import logging
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import GeneratePopcornRequest
from image_processor import analyze_image
from llm_client import generate_flavor_suggestion
import datetime
import aiofiles
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Default React dev server port
    "http://localhost:5173",  # Default Vite dev server port
    "http://localhost:5174",  # Alternative Vite port
    "http://localhost:1234",  # Example port for Electron
    "app://.",
    "file://",
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

def log_session(name: str, mood: str, image_filename: str, flavor: str):
    """Appends session data to the CSV file."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'name', 'mood', 'image_filename', 'flavor']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': datetime.datetime.now().isoformat(),
            'name': name,
            'mood': mood,
            'image_filename': image_filename,
            'flavor': flavor,
        })

@app.on_event("startup")
async def startup_event():
    logging.info("Moocorn backend starting up.")

@app.get("/")
def read_root():
    return {"message": "Moocorn backend is running!"}


@app.post("/generate_popcorn")
async def generate_popcorn(
    name: str = Form(...),
    mood: str = Form(...),
    image: UploadFile = File(None)
):
    logging.info(f"Received popcorn generation request for name: {name}, mood: {mood}, has_image: {image is not None}")
    start_time = datetime.datetime.now()
    
    image_filename = None
    analysis_results = {}
    
    if image is not None:
        # Save the image
        image_filename = f"{start_time.strftime('%Y%m%d_%H%M%S')}_{name}.jpg"
        image_path = f"data/images/{image_filename}"
        
        try:
            async with aiofiles.open(image_path, 'wb') as out_file:
                content = await image.read()
                await out_file.write(content)
            logging.info(f"Image saved to {image_path}")
        except Exception as e:
            logging.error(f"Error saving image: {e}")
            raise HTTPException(status_code=500, detail="Error saving image")

        # Analyze the image
        logging.info(f"Analyzing image: {image_path}")
        analysis_results = analyze_image(image_path)
        if analysis_results.get("error"):
            logging.error(f"Image analysis failed: {analysis_results['error']}")
            raise HTTPException(status_code=500, detail=f"Image analysis failed: {analysis_results['error']}")
        logging.info(f"Image analysis successful: {analysis_results}")
    else:
        logging.info("No image provided, proceeding without image analysis")
        analysis_results = {"lightness": "unknown", "dominant_color_names": ["mysterious"]}

    # Generate flavor suggestion
    logging.info("Generating flavor suggestion from LLM.")
    suggestion = generate_flavor_suggestion(name, mood, analysis_results)
    if suggestion.get("error"):
        logging.error(f"LLM request failed: {suggestion['error']}")
        raise HTTPException(status_code=500, detail=f"LLM request failed: {suggestion['error']}")
    logging.info(f"LLM suggestion received: {suggestion}")

    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    logging.info(f"Flavor generation took {duration:.2f} seconds.")

    # Log the session
    log_session(
        name=name,
        mood=mood,
        image_filename=image_filename or "no_image",
        flavor=suggestion.get("flavor", ""),
    )
    logging.info("Session logged to CSV.")

    return {
        "message": "Popcorn generated successfully!",
        "flavor": suggestion.get("flavor"),
        "image_analysis": analysis_results,
        "duration": duration,
    }

