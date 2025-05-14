import json

def get_token():
    with open('data/token.json', 'r') as file:
        data = json.load(file)
    token = data['token']
    return token