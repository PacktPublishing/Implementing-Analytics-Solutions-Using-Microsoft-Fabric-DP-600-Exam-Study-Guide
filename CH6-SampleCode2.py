import json

data = {
    'customers': [
        {'id': 1, 'name': 'Alice', 'purchase': 100},
        {'id': 2, 'name': 'Bob', 'purchase': 200}
    ]
}
json_data = json.dumps(data, indent=4)
with open('data.json', 'w') as f:
    f.write(json_data)
