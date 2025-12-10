import yaml
import json

with open ("config.yaml") as f:
    data = yaml.safe_load(f)

json_data = json.dumps(data, indent=4)

with open ("config.json", "w") as f:
    f.write(json_data)

print("Yaml file converted to JSON successfully!")