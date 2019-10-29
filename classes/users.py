class User():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("The first name of the user is: "+self.first_name.title())
        print("The last name of the user is: "+self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name.title())

my_user1 = User("lucy","scarlet")
my_user2 = User("peter","parker")
my_user3 = User("croco","drile")
my_user4 = User("jack","sparrow")

my_user1.describe_user()
my_user1.greet_user()

my_user2.describe_user()
my_user2.greet_user()

my_user3.describe_user()
my_user3.greet_user()

my_user4.describe_user()
my_user4.greet_user()