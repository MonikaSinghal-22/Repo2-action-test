import argparse
import sys
import json
import os

def main(repository_name, version, user, input_data):
    # if len(sys.argv) < 3:
    #     print("❌ Error: Missing required arguments.")
    #     sys.exit(1)

    # #repository_name = sys.argv[1]
    # repository_name = sys.argv[1] if sys.argv[1] else os.getenv("GITHUB_REPOSITORY", "unknown_repo")
    # version = sys.argv[2]
    # input_data = sys.argv[3]
    
    if not repository_name:
        repository_name = os.getenv("GITHUB_REPOSITORY")
    
    print(repository_name)
    print(version)
    print(user)
    print(input_data)
    print(type(input_data))

    try:
        # Convert input_data from string to JSON
        input_json = json.loads(input_data)
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format in input-data.")
        sys.exit(1)

    # Construct the formatted output
    formatted_data = {
        "release": {
            "repo_name": repository_name,
            "version": version,
            "user": user
        },
        "user": input_json.get("user", ""),
        "data": input_json.get("data", "")
    }

    # Save formatted JSON to file
    with open("formatted_data.json", "w") as json_file:
        json.dump(formatted_data, json_file, indent=4)

    print("✅ Successfully validated and saved formatted data.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate input JSON and call an API.")

    parser.add_argument("--repository_name", type=str,
                        help="Repository name (defaults to GitHub repository if empty)")
    parser.add_argument("--version", type=str, required=True, help="Version of the release")
    parser.add_argument("--user", type=str, required=True, help="user of the release")
    parser.add_argument("--input_data", type=str, required=True, help="JSON input data")

    args = parser.parse_args()

    main(args.repository_name, args.version, args.user, args.input_data)
    
