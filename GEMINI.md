# Moocorn Codebase - Gemini's Perspective

This document provides an overview of the Moocorn project codebase, as understood and implemented by Gemini.

## Architecture

The application is a desktop app built with a Python backend and a React/Electron frontend.

- **Backend**: A FastAPI server handles the core logic, including image processing with OpenCV and LLM interaction with a LocalAI server.
- **Frontend**: A React application, wrapped in Electron, provides the user interface.
- **Communication**: The frontend and backend communicate via a REST API.

## Project Structure

```
moocorn/
├── backend/            # Python FastAPI backend
│   ├── data/
│   │   ├── images/     # Saved user images
│   │   ├── flavors.txt # List of available popcorn flavors
│   │   └── sessions.csv# Log of user sessions
│   ├── main.py         # FastAPI server application
│   ├── image_processor.py # OpenCV image analysis logic
│   ├── llm_client.py   # LocalAI integration
│   ├── models.py       # Pydantic data models
│   └── pyproject.toml  # Python dependencies
├── frontend/           # React/Electron frontend
│   ├── src/            # React source code
│   └── ...
├── .gitignore          # Git ignore file
├── README.md           # Project README
├── GEMINI.md           # This file
└── CLAUDE.md           # Claude's perspective
```

## Backend Details

The backend is a FastAPI application with the following key components:

- `main.py`: Defines the main FastAPI application, including CORS configuration, API endpoints, and session logging.
- `image_processor.py`: Contains functions for analyzing images using OpenCV, such as calculating average color, brightness, and dominant colors.
- `llm_client.py`: Manages communication with the LocalAI server, including reading the flavor list, constructing prompts, and sending requests to the LLM.
- `models.py`: Defines the Pydantic models for API request and response validation.
- `pyproject.toml`: Manages Python dependencies using `uv`.

## Frontend Details

The frontend is a React application that will be initialized using `pnpm` and `create-react-app`. It will be packaged as a desktop application using Electron.


Implementation Plan:

  Phase 1: Backend Foundation

  1. FastAPI Setup
    - Basic server with CORS for Electron
    - Health check endpoint
    - File upload handling
  2. Image Processing Module
    - Average color calculation
    - Dominant color extraction
    - Brightness analysis
    - Texture analysis (chaos detection)
    - Color histogram generation
  3. Data Models
    - Request/response schemas
    - Image analysis results structure

  Phase 2: LLM Integration

  1. LocalAI Client
    - OpenAI-compatible API calls
    - Prompt engineering for popcorn flavor generation
    - Error handling for LLM failures
  2. Flavor Management
    - Read flavors from TXT file
    - Hot-reload capability for flavor updates

  Phase 3: Frontend Development

  1. Electron + React Setup
    - Basic Electron window configuration
    - React development environment
    - Build pipeline
  2. Screen Components
    - Welcome screen with name input
    - Mood selection screen
    - Camera interface with live preview
    - Progress/loading screen
    - Results display screen
  3. Navigation & State
    - Screen routing
    - Persistent cancel/home button
    - State management across screens

  Phase 4: Camera Integration

  1. Camera Access
    - WebRTC camera permissions
    - Photo capture functionality
    - Image preview before submission
  2. File Handling
    - Image upload to backend
    - Error handling for camera issues

  Phase 5: Data Persistence

  1. Session Logging
    - CSV format: timestamp, name, mood, image_file, generated_flavor
    - Unique filename generation for images
    - Error logging

  Phase 6: Integration & Testing

  1. End-to-End Flow
    - Complete user journey testing
    - Error state handling
    - Performance optimization
  2. LocalAI Setup
    - Integration documentation
    - Fallback mechanisms if LLM unavailable

  Key Technical Decisions

  1. Electron vs. Tauri: Electron chosen for mature React ecosystem and easier camera access
  2. Image Processing: Keep it simple with OpenCV basics to avoid overwhelming the LLM
  3. State Management: Basic React state (useState/useContext) should suffice
  4. File Storage: Simple filesystem approach for prototyping, can upgrade later
  5. Error Handling: Graceful degradation if LLM/camera unavailable

  Development Commands (to be created)

  # Backend
  cd backend && python -m uvicorn main:app --reload

  # Frontend
  cd frontend && npm start

  # Build for production
  npm run build

  Next Steps

  1. Would you like me to start implementing this plan?
  2. Any modifications to the architecture or flow?
  3. Do you have specific requirements for the LocalAI setup?

  The plan is designed to be modular so we can build and test each component independently before integration.