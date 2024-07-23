import yaml
import json

def convert_yaml_to_json(yaml_file_path, json_file_path):
    with open(yaml_file_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    json_data = json.dumps(yaml_data, indent=4)

    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

convert_yaml_to_json('my_yaml_file.yaml', 'my_json_file.json')