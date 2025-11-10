#!/bin/bash

# Script to run the Streamlit app locally

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run Streamlit app
echo "Starting Streamlit app..."
echo ""
echo "🚀 Your app will be available at: http://localhost:8501"
echo ""
streamlit run app.py

