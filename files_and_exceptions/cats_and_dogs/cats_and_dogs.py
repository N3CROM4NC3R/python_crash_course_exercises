filename_cats = "cats.txt"
filename_dogs = "dogs.txt"
try:
    with open(filename_cats,'r') as file_object:
        cats_name = file_object.readlines()
        print("Cats names:")
        for cat_name in cats_name:
            print(cat_name)

except FileNotFoundError:
    print("The file of the cat names not exist")

try:
    with open(filename_dogs,'r') as file_object:
        dogs_name = file_object.readlines()
        print("Dogs names:")
        for dog_name in dogs_name:
            print(dog_name)

except FileNotFoundError:
    print("The file of the dog names not exist")
