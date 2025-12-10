import yaml

with open ("config.yaml") as f:
    data = yaml.safe_load(f)

print(data)

data['app']['version'] = 2.0
data['database'] = {}
data['database']['user'] = "root"
data['database']['host'] = 'localhost'

with open ("config1.yml", "w") as f:
    yaml.dump(data, f)