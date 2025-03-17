#!/bin/bash

echo "🚀 Running Validation in Docker Action..."

# Save input-data to a file
echo "$INPUT_JSON" > input.json

# Run validation script
python /app/validate.py
