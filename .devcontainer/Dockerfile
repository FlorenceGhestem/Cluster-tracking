FROM python:3.8-slim

# Install any required system packages here
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /cluster-tracking

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the rest of your application files into the container
COPY . .
