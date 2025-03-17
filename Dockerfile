# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY validate.py /app/validate.py
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Install dependencies (if needed)
#RUN pip install requests

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
