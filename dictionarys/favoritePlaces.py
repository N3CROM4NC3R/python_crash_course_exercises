favoritePlaces = {
    "diana" : {
        "name" : "cataratas del niagara",
        "location": ["canada"]
    },
    "santiago" : {
        "name" : "the blue lagoon",
        "location" : ["iceland"]
    },
    "marcus" : {
        "name" : "himalaya",
        "location" : ["butan","nepal","china","india","pakistan"]
    }
}



for name,information in favoritePlaces.items():
    print("The favorite place of "+name+" is:")
    for name,location in information.items():
        print("The name is:"+name+",The location:")
        if len(location)==1:
            print(location)
        else:
            for country in location:
                print(country)
            print("\n")
