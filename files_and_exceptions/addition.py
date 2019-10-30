try:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
except TypeError:
    print("Just numbers please")
else:
    print(first_number+second_number)
