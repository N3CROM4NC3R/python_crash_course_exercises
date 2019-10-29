class Admin():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_privilege(self):
        print("admin")


class User():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0

    def describe_user(self):
        print("The first name of the user is: "+self.first_name.title())
        print("The last name of the user is: "+self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello " + full_name.title())

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0
