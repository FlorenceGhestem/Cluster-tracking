# Use Python 3.9 as the base image to ensure compatibility with all libraries
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /cluster-tracking

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Command to run when the container starts
CMD ["python", "src/python/cluster_tracking.py"]
