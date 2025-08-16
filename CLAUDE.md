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

1.  **Phase 1: Backend Foundation**: Set up the FastAPI server, CORS, and basic endpoints.
2.  **Phase 2: LLM Integration**: Connect to the LocalAI server and implement prompt engineering.
3.  **Phase 3: Frontend Development**: Set up the React/Electron environment and create the UI components.
4.  **Phase 4: Camera Integration**: Implement camera access and image capture.
5.  **Phase 5: Data Persistence**: Implement CSV logging and image storage.
6.  **Phase 6: Integration & Testing**: Perform end-to-end testing and error handling.
