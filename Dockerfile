FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY hello_world.py .
COPY requirements.txt .
COPY test_hello_world.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by Flask
EXPOSE 4049

# Command to run the application
CMD ["python", "hello_world.py"]
