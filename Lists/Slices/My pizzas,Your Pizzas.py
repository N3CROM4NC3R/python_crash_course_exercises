pizzas=["chesse pizza","cheddar pizza","detroit pizza"]

friendPizzas=pizzas[:]
pizzas.append("new york pizza")
friendPizzas.append("greek pizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:",friendPizza)
for friendPizza in friendPizzas:
    print(friendPizza)