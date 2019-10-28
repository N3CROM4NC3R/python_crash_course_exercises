def make_car(manufacturer,model,**information):
    car = {
        "manufacturer" : manufacturer,
        "model" : model,
    }

    for key,value in information.items():
        car[key] = value

    return car

car = make_car('subaru','outback',color='blue',tow_package=True)

for key,value in car.items():
    print(key," => ",value)prpp