import yaml

with open ("config.yaml") as f:
    data = yaml.safe_load(f)
    print(data)

#adding a comment to check the git