sandwich_orders = ["meat sandwich","pastrami","chesse sandwich","pig sandwich","sausage sandwich",
                   "pastrami","pastrami"]

print("The deli has run out of pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("The new orders are:")
for sandwich in sandwich_orders:
    print(sandwich)
