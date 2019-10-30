filename_cats = "catss.txt"
filename_dogs = "dogss.txt"
try:
    with open(filename_cats,'r') as file_object:
        cats_name = file_object.readlines()
        print("Cats names:")
        for cat_name in cats_name:
            print(cat_name)

except FileNotFoundError:
    pass

try:
    with open(filename_dogs,'r') as file_object:
        dogs_name = file_object.readlines()
        print("Dogs names:")
        for dog_name in dogs_name:
            print(dog_name)

except FileNotFoundError:
    pass
