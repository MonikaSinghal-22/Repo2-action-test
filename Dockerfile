# Use official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files into the container
COPY validate.py ./app/validate.py

# Install dependencies if needed
RUN pip install requests  # Add any required dependencies

# Set entrypoint to execute the validation script
ENTRYPOINT ["python", "/app/validate.py"]
