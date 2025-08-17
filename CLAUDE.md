# Moocorn Codebase - Claude's Plan

This document outlines the project plan for Moocorn, as proposed by Claude. This plan serves as the roadmap for the development of the application.

## Architecture Overview

- **Tech Stack**:
  - **Frontend**: React + Electron
  - **Backend**: Python FastAPI
  - **Image Processing**: OpenCV
  - **LLM**: LocalAI (OpenAI-compatible)
  - **Data Storage**: CSV for logs, TXT for flavors
- **Communication**: REST API between frontend and backend.

## Project Structure

```
moocorn/
├── backend/
│   ├── main.py
│   ├── image_processor.py
│   ├── llm_client.py
│   ├── models.py
│   ├── requirements.txt (now pyproject.toml)
│   └── data/
│       ├── flavors.txt
│       ├── sessions.csv
│       └── images/
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── WelcomeScreen.js
│   │   │   ├── MoodScreen.js
│   │   │   ├── CameraScreen.js
│   │   │   ├── ProgressScreen.js
│   │   │   └── ResultScreen.js
│   │   └── utils/
│   │       └── api.js
│   └── public/
└── README.md
```

## Implementation Plan

The project is broken down into the following phases:

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