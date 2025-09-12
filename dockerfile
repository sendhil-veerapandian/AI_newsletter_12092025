# Use an official Python runtime as a base image
FROM python:3.11-slim-bookworm

# Set environment variables to prevent Python from writing pyc files and buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first for better caching
COPY requirements.txt .

# Install system dependencies required for some Python packages (like for crewai_tools, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Streamlit runs on by default
EXPOSE 8501

# Define the command to run the Streamlit app
# Use the host 0.0.0.0 to make it available outside the container
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
