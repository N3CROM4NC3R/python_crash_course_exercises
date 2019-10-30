import json

def get_favorite_number():
    favorite_number = input("Insert your favorite number:")
    filename = 'favorite_number.json'
    with open(filename,'w') as file_object:
        json.dump(favorite_number,file_object)
    return favorite_number

def get_stored_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename,'r') as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

print("Hello user,Welcome to the FAVORITE NUMBER CLUB!")
favorite_number = get_stored_favorite_number()
if favorite_number:
    print("Hello.i remember than your favorite number is: "+favorite_number)
else:
    favorite_number = get_favorite_number()
    print("Hello,i will remember your favorite number for the next time :D: "+favorite_number)
