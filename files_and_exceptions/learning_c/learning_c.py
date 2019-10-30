filename = 'learning_c.txt'

with open(filename) as file_object:
    lines = file_object.read()

print(lines.replace("python","c"))