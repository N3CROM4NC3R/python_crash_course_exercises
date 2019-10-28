peoples1 = {
    "maria" : {
        "first" : "maria",
        "last" : "gonzalez",
        "age" : "51",
        "city" : "valle de la pascua"
    },
    "fernando" : {
        "first" : "fernando",
        "last" :"perez",
        "age" : "27",
        "city": "valle de la pascua"
    },
    "nestor" :{
        "first" : "nestor",
        "last" : "perez",
        "age" : "33",
        "city" : "valle de la pascua"
    }
}
peoples2 = {
    "santiago" : {
        "first" : "santiago",
        "last" : "padron",
        "age" : "18",
        "city" : "valle de la pascua"
    },
    "jose" : {
        "first" : "jose",
        "last" :"perez",
        "age" : "52",
        "city": "valle de la pascua"
    },
    "suheidy" :{
        "first" : "suheidy",
        "last" : "perez",
        "age" : "37",
        "city" : "valle de la pascua"
    }
}

for name,information in peoples1.items():
    print("Information of",name)
    for key,value in information.items():
        print(key + ":" + value)
    print("\n")

for name,information in peoples2.items():
    print("Information of",name)
    for key,value in informationpe.items():
        print(key + ":" + value)
    print("\n")