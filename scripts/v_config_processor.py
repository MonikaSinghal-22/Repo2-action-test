import argparse
import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser()
    parser.add('--config', default="config/v_config.yaml")
    args = parser.parse_args()
    
    v_config = load_yaml(args.config)
    
    print(f"loaded from '{args.config}'")
    
    print(v_config)

if __name__ == "__main__":
    main()