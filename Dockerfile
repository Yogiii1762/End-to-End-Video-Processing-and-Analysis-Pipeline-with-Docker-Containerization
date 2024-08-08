
# Use a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage caching
COPY requirements.txt /app/

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Command to run the application
CMD ["python", "main.py"]
