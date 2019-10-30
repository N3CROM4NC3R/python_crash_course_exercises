filename = 'programming_poll.txt'
flag_activate = True
option = ''

with open(filename,'a') as file_object:
    while flag_activate:
        reason = input("Insert a reason about why you programming:")
        file_object.write(reason+"\n")

        option = input("Wanna you insert other reason(Yes/No)?:")

        if option.lower() == 'no':
            flag_activate = False