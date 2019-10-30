filename_cats = "cats.txt"
filename_dogs = "dogs.txt"

with open(filename_cats,'w') as file_object:
    cats_name = ["fuffy","garfield","tom"]
    for cat_name in cats_name:
        file_object.write(cat_name+'\n')

with open(filename_dogs,'w') as file_object:
    dogs_name = ["doggy","sam","boston"]
    for dog_name in dogs_name:
        file_object.write(dog_name+'\n')

