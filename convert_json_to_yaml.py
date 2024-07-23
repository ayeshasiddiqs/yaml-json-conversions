import json
import yaml

def convert_json_to_yaml(json_file_path, yaml_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(json_data, yaml_file, default_flow_style=False)

convert_json_to_yaml('my_json_file.json', 'my_yaml_file.yaml')
