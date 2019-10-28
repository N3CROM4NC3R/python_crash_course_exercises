def sandwiches(*toppings_sandwiches):
    for topping in toppings_sandwiches:
        print("This sandwich was ordered: "+topping)

sandwiches("Chesse sandwich")
sandwiches("Meat sandwich","Vegetarian sandwich")
sandwiches("Greek sandiwch","Club sandwich","Hero sandwich","Pocket Sandwich")
