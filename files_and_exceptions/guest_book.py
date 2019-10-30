flag_activate = True
option = ''
filename = "guest_book.txt"

with open(filename,'a') as file_object:
    while flag_activate:
        first_name = input("Insert your first name dear user:")
        last_name = input("Now,insert your last name dear user:")

        file_object.write(first_name+' '+last_name+'\n')

        option = input("wanna you insert other guest(Yes/No)?:")
        if option.lower() == 'no':
            flag_activate = False
