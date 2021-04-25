import json

with open('zadacha-7(dump).txt') as json_ob:
    text = json.load(json_ob)
print(type(text))