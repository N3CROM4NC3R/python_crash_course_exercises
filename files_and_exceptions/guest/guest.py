first_name = input("Insert your first name dear user:")
last_name = input("Now,insert your last name dear user:")

filename = "guest.txt"

with open(filename,'a') as file_object:
    file_object.write(first_name+" "+last_name+"\n")