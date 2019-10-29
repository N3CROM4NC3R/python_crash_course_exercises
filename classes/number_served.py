class Restaurant():

    def __init__(self,restaurant_name,cuisine_name,number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is: "+self.restaurant_name.title())
        print("The name of the cuisine is: "+self.cuisine_name.title())

    def open_restaurant(self):
        print("The restaurant is now openning")

    def set_number_served(self,number_served):
        self.number_served = number_served
        print(self.number_served)

    def increment_number_served(self):
        self.number_served += 1


my_restaurant = Restaurant("panaderia nina","cocinita",0)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(9)
my_restaurant.increment_number_served()

print("The number of served of this restaurant is: "+str(my_restaurant.number_served))