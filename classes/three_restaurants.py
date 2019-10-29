class Restaurant():

    def __init__(self,restaurant_name,cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print("The name of the restaurant is: "+self.restaurant_name.title())
        print("The name of the cuisine is: "+self.cuisine_name.title())

    def open_restaurant(self):
        print("The restaurant is now openning")

my_restaurant = Restaurant("panaderia nina","cocinita")
my_restaurant2 = Restaurant("italyc delicious","cheffyer")
my_restaurant3 = Restaurant("Venezuela Yummy","Chavez")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant2.describe_restaurant()
my_restaurant2.open_restaurant()

my_restaurant3.describe_restaurant()
my_restaurant3.open_restaurant()
