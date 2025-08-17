#!/bin/bash

# --- Configuration ---
# Set default ports or use environment variables if they are defined
MOOCORN_BACKEND_PORT=${MOOCORN_BACKEND_PORT:-8000} # Default to 8000 if MOOCORN_BACKEND_PORT env var is not set
MOOCORN_FRONTEND_PORT=${MOOCORN_FRONTEND_PORT:-3000} # Default to 3000 if MOOCORN_FRONTEND_PORT env var is not set
# --- End Configuration ---

# Function to check if a port is in use
check_port() {
  PORT=$1
  SERVICE_NAME=$2
  echo "Checking if $SERVICE_NAME port $PORT is in use..."
  # Use lsof to check if the port is in use. Redirect output to /dev/null to suppress it.
  if lsof -i :$PORT >/dev/null 2>&1; then
    echo "Error: $SERVICE_NAME port $PORT is already in use. Please free up the port or kill the existing process."
    exit 1
  else
    echo "$SERVICE_NAME port $PORT is available."
  fi
}

# Function to start the backend
start_backend() {
  echo "Starting backend on port $MOOCORN_BACKEND_PORT..."
  cd backend && uvicorn main:app --port $MOOCORN_BACKEND_PORT --reload &
  BACKEND_PID=$!
  echo "Backend started with PID: $BACKEND_PID"
}

# Function to start the frontend
start_frontend() {
  echo "Starting frontend on port $MOOCORN_FRONTEND_PORT..."
  # npm start typically uses the PORT environment variable
  cd frontend && PORT=$MOOCORN_FRONTEND_PORT npm start &
  FRONTEND_PID=$!
  echo "Frontend started with PID: $FRONTEND_PID"
}

# Main script logic
echo "Moocorn Application Launcher"
echo "---------------------------"

# Check ports before launching any services
check_port $MOOCORN_BACKEND_PORT "Backend"
check_port $MOOCORN_FRONTEND_PORT "Frontend"

start_backend
start_frontend

echo "All services launched. Press Ctrl+C to stop."

# Wait for all background processes to finish (or for Ctrl+C)
wait