import yaml

with open ("config.yaml") as f:
    data = yaml.safe_load(f)

print(data)

data['app']['version'] = 2.0

with open ("config1.yml", "w") as f:
    yaml.dump(data, f)