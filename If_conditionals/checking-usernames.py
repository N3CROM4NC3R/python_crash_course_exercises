currentUsers = ["santi123","libardozene","coxato","edsel","admin","blanquito"]
newUsers = ["angelo","croco","santi123","libardozene","coxato"]

for user in newUsers:
    if user.lowepr() not in currentUsers:
        currentUsers.append( user )
        print("The user " + user + " is now a currentUser :D")
    else:
        print("The user " + user + " is a repetead user")
print("The currentUsers are :", currentUsers)
