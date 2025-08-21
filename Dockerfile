# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY todo-app .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the cli.py on startup
CMD ["python", "cli.py"]
