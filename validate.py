import json
import sys

# Load input JSON
with open("input.json", "r") as f:
    data = json.load(f)

# Extract values
user = data.get("user")
input_data = data.get("data")

# Validation logic
if not user or not input_data:
    print("❌ Validation Failed: 'user' or 'data' is missing.")
    sys.exit(1)  # Exit with failure code

if not input_data.isdigit():
    print("❌ Validation Failed: 'data' must be numeric.")
    sys.exit(1)

print("✅ Validation Passed: Input is valid.")
sys.exit(0)