# Moocorn - The Intelligent Popcorn Machine

Moocorn is a generative AI popcorn flavor maker. It takes a user's name, mood, and a picture to generate a unique popcorn flavor suggestion with a witty and whimsical description.

This project is designed to be a desktop application using Electron, but it can also be run as a web application.

## Features

-   **Personalized Popcorn Flavors**: Get a unique popcorn flavor based on your name, mood, and a picture.
-   **Image Analysis**: Uses OpenCV to analyze the image for color, brightness, and other features.
-   **LLM Integration**: Connects to LocalAI, OpenAI, or OpenRouter to generate creative flavor suggestions.
-   **Desktop & Web**: Can be run as a desktop application or a web application.

## Architecture

-   **Frontend**: React (with TypeScript and Vite), packaged with Electron.
-   **Backend**: Python (with FastAPI and Pydantic).
-   **Image Processing**: OpenCV.
-   **LLM**: LocalAI, OpenAI, or OpenRouter.

## Installation

### Backend

1.  **Clone the repository**

2.  **Navigate to the `backend` directory**

    ```bash
    cd backend
    ```

3.  **Create a virtual environment and install dependencies**

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install uv # if you don't have uv installed
    uv pip install --with-sources . # install from pyproject.toml
    ```

4.  **Configure your LLM provider**

    -   **For LocalAI**: No API key is needed. Ensure your LocalAI server is running.
    -   **For OpenAI or OpenRouter**: Create a `.env` file in the `backend` directory and add your API key and other settings:

        ```
        LLM_PROVIDER=openai # or openrouter
        LLM_API_KEY=your_api_key
        LLM_MODEL=your_model_name
        ```

### Frontend

1.  **Navigate to the `frontend` directory**

    ```bash
    cd frontend
    ```

2.  **Install dependencies using pnpm**

    ```bash
    pnpm install
    ```

## Running the Application

### Backend

To run the backend server, navigate to the `backend` directory and run:

```bash
uv uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend (Web)

To run the frontend as a web application, navigate to the `frontend` directory and run:

```bash
pnpm dev
```

This will start a development server, and you can access the application at `http://localhost:5173`.

### Frontend (Electron)

(Instructions to be added once Electron setup is complete.)
