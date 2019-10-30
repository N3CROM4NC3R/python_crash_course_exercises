import json

cube = list(value **3 for value in range(10))

filename = 'cubes.json'

with open(filename,'w') as f_obj:
    json.dump(cube,f_obj)