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
