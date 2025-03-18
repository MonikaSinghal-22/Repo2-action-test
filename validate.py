import sys
import json

def main():
    print(len(sys.argv))
    print(sys.argv[4])
    if len(sys.argv) < 3:
        print("❌ Error: Missing required arguments.")
        sys.exit(1)

    repository_name = sys.argv[1]
    version = sys.argv[2]
    input_data = sys.argv[3]
    
    print(repository_name)
    print(version)
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
            "version": version
        },
        "user": input_json.get("user", ""),
        "data": input_json.get("data", "")
    }

    # Save formatted JSON to file
    with open("formatted_data.json", "w") as json_file:
        json.dump(formatted_data, json_file, indent=4)

    print("✅ Successfully validated and saved formatted data.")

if __name__ == "__main__":
    main()
