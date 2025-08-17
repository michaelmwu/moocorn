# Moocorn - The Intelligent Popcorn Machine

Moocorn is a generative AI popcorn flavor maker. It takes a user's name, mood, and a picture to generate a unique popcorn flavor suggestion with a witty and whimsical description.

This project is designed to be a desktop application using Electron, but it can also be run as a web application.

[Demo video](https://www.dropbox.com/scl/fi/8yyaexabxi7ae4ynqo4ng/MooCorn-demo.mov?rlkey=0bewggiup55yb8zhpg4bh6lng&st=vep9pvnn&dl=0)

## Features

-   **Personalized Popcorn Flavors**: Get a unique popcorn flavor based on your name, mood, and a picture.
-   **Image Analysis**: Uses OpenCV to analyze the image for color, brightness, and other features.
-   **LLM Integration**: Connects to a local LLM server using Ollama or LocalAI, or to remote services like OpenAI or OpenRouter.
-   **Desktop & Web**: Can be run as a desktop application or a web application.

## Architecture

-   **Frontend**: React (with TypeScript and Vite), packaged with Electron.
-   **Backend**: Python (with FastAPI and Pydantic).
-   **Image Processing**: OpenCV.
-   **LLM**: Ollama, LocalAI, OpenAI, or OpenRouter.

## Installation

1.  **Install `uv` (if you haven't already)**

    We recommend installing `uv` globally. For macOS/Linux, you can typically run:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Install Backend Dependencies**
    ```bash
    cd backend
    uv pip install -e .
    cd ..
    ```

3.  **Install Frontend Dependencies**
    ```bash
    cd frontend
    pnpm install
    cd ..
    ```

4.  **Configure your LLM provider**

    Copy the `.env.example` file to a new `.env` file and customize it for your setup.
    ```bash
    cp .env.example .env
    ```

    -   **For Ollama**: No API key is needed. Ensure Ollama is running. The default settings in `.env.example` should work.
    -   **For OpenAI or OpenRouter**: Edit the `.env` file with your API key and other settings:
        ```
        LLM_PROVIDER=openai # or openrouter
        LLM_API_KEY=your_api_key
        LLM_MODEL=your_model_name
        LLM_BASE_URL=https://api.openai.com/v1 # or your OpenRouter URL
        ```

## Running the Application

### Using Docker (Recommended)

This is the simplest way to get started. It will build and run both the frontend and backend with live-reloading.

```bash
COMPOSE_BAKE=true docker compose watch
```

### Running Manually

#### Backend

To run the backend server, navigate to the `backend` directory and run:

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8888
```

#### Frontend

To run the frontend as a web application, navigate to the `frontend` directory and run:

```bash
pnpm dev
```

This will start a development server, and you can access the application at `http://localhost:5173`.

#### Frontend (Electron)

To run the application in an Electron window, navigate to the `frontend` directory and run:

```bash
pnpm dev:electron
```

**Note:** If Electron fails to start, you may need to run its installation script manually:
```bash
node node_modules/electron/install.js
```
