# Use official Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
# EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "web.py", "--server.port=8501", "--server.address=0.0.0.0"]
