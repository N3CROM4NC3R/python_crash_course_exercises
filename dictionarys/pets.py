pets = {
    "puddy" : {
        "kind" : "dog",
        "name" : "puddy"
    },
    "pete" : {
        "kind" : "koala",
        "name" : "pete"
    },
    "platon" : {
        "kind" : "monkey",
        "name" : "platon"
    }
}
for name,information in pets.items():
    print("The information of the pet:",name,"is:")
    for key,value in information.items():
        print(key,"=>",value)
    print("\n")