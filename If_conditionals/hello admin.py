users = ["santi123","libardozene","coxato","edsel","admin","blanquito"]
user = "santi123"
if user in users:
    if user == "admin":
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello " + user + ",thank you for logging in again.")