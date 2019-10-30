while True:
    try:
        first_number = int(input("First number: "))
        second_number = int(input("Second number: "))
    except ValueError:
        print("Just numbers please")
    else:
        print(first_number+second_number)
