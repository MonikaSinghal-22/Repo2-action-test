#!/bin/bash
set -e

EMPTY_TEST=$1
REPO_NAME=$1
VERSION=$2
INPUT_DATA=$3

# If repository_name is empty, use the GitHub repository value
if [[ -z "$REPO_NAME" ]]; then
  REPO_NAME="${GITHUB_REPOSITORY}"
fi

echo "Repository Name: $REPO_NAME"
echo "Version: $VERSION"
echo "Input Data: $INPUT_DATA"

# Run validation script
python /app/validate.py "$REPO_NAME" "$VERSION" "$INPUT_DATA" "$EMPTY_TEST"
