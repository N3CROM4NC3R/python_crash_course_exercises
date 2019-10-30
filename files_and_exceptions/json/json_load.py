import json
filename = 'cubes.json'

with open(filename) as file_object:
    cube = json.load(file_object)
print(cube)