import json


with open('data/BoardsCorrect.json', 'r') as file:
    data = json.load(file)

print(data[3])