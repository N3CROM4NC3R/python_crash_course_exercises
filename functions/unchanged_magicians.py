def show_magicians(names):
    print("Welcome to the show of the Greats:\nOur magicians are:")
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i]="The Great "+names[i]
    return names

magicians = ["carlos","pedro","ignacio"]

make_great(magicians)
new_names_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(new_names_magicians)
