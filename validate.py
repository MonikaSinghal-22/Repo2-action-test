import argparse
import base64
import sys
import json
import os
import requests

def main(repository_name, version, release_type, user,checksum_data, team_name, organization, input_data, base_url):
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
    print(release_type)
    print(user)
    print(checksum_data)
    print(team_name)
    print(organization)
    print(base_url)
    print(input_data)
    print(type(input_data))
    
    if checksum_data:
        checksum_data_json = json.loads(checksum_data)
        for checksum in checksum_data_json:
            if not isinstance(checksum, dict):
                print("❌ Error: Invalid JSON format in checksum dictionary.")
                sys.exit(1)
            for key, _ in checksum.items():
                #print(key)
                pass
    try:
        # Convert input_data from string to JSON
        input_json = json.loads(base64.b64decode(input_data).decode())
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format in input-data.")
        sys.exit(1)

    # Construct the formatted output
    formatted_data = {
        "release": {
            "repo_name": repository_name,
            "version": version,
            "release_type": release_type,
            "user": user,
            "team_name": team_name,
            "checksum": checksum_data_json
        },
        "user": input_json.get("user", ""),
        "data": input_json.get("data", "")
    }

    # Save formatted JSON to file
    with open("formatted_data.json", "w") as json_file:
        json.dump(formatted_data, json_file, indent=4)
        
    response = requests.post("https://jsonplaceholder.typicode.com/todos/1")
    print(response)

    print("✅ Successfully validated and saved formatted data.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate input JSON and call an API.")

    parser.add_argument("--repository_name", type=str,
                        help="Repository name (defaults to GitHub repository if empty)")
    parser.add_argument("--version", type=str, required=True, help="Version of the release")
    parser.add_argument("--release_type", type=str, required=True, help="Release type")
    parser.add_argument("--user", type=str, required=True, help="user of the release")
    parser.add_argument("--checksum_data", type=str, required=False, help="checksum")
    parser.add_argument("--team_name", type=str, required=True, help="team")
    parser.add_argument("--organization", type=str, required=True, help="org")
    parser.add_argument("--input_data", type=str, required=True, help="JSON input data")
    parser.add_argument("--base_url", type=str, required=False, help="API base url")

    args = parser.parse_args()

    main(args.repository_name, args.version, args.release_type, args.user, args.checksum_data, args.team_name, args.organization, args.input_data, args.base_url)
    
