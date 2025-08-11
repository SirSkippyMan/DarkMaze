#!/bin/bash

set -e  # Exit on any error

echo "Checking for Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Please install Python 3 and try again."
    exit 1
fi

echo "Creating virtual environment (if not already present)..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running the game..."
python3 main.py

deactivate