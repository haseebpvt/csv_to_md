FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY .streamlit .streamlit

# Expose port 8080 (required for Cloud Run)
EXPOSE 8080

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health || exit 1

# Run the application
# Cloud Run sets PORT environment variable, default to 8080
CMD streamlit run app.py --server.port=${PORT:-8080} --server.address=0.0.0.0

