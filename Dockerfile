# Use official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /github/workspace

# Copy necessary files into the container
COPY validate.py .

# Install dependencies if needed
RUN pip install requests  # Add any required dependencies

# Set entrypoint to execute the validation script
ENTRYPOINT ["python", "validate.py"]
