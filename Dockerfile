# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8080

# Define environment variable

# Run Battleship.py when the container launches
CMD ["python3", "Battleship.py", "--port", "8080"]