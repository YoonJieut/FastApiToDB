import json

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

with open('output.json', 'w') as f:
    json.dump(data, f)
