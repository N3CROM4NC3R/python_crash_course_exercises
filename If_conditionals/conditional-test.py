favoriteFood="hotcakes"

print("Is your favoriteFood==hotcakes? I predict true:")
print(favoriteFood == 'hotcakes')
print(favoriteFood.upper() == "HOTCAKES")
print(favoriteFood.lower() == "hotcakes")
print(favoriteFood.title() == "Hotcakes")
print(favoriteFood.count("hotcakes") == 1)

print("\nIs your favoriteFood == hotdogs?I predict false:")
print(favoriteFood == 'hotdogs')
print(favoriteFood.title() == 'hotcakes')
print(favoriteFood.upper() == 'hotcakes')
print(favoriteFood.lower() == 'HOTCAKES')
print(favoriteFood.capitalize() == 'hotcakes')
