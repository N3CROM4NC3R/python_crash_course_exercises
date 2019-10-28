favoriteNumbers={
    "santiago":[8,11],
    "libardo" :[5,2],
    "carlos"  :[1,9],
    "edsel"   :[2,4],
    "angel"   :[0,19]
}

for name,numbers in favoriteNumbers.items():
    print("The person "+name+" Have the followers numbers:")
    for number in numbers:
        print(number)