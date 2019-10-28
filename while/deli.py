sandwich_orders = ["meat sandwich","chesse sandwich","pig sandwich","sausage sandwich"]
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your "+sandwich)
    finished_sandwich.append(sandwich)

print("The sandwich than i made are: ")
for sandwich in finished_sandwich:
    print(sandwich)