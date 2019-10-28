polls = []
active = True

while active:
    question = input("You could visit a place?(Yes/No):")
    if question.lower() == "no":
        active = False
        continue
    place = input("Which is the place?:")
    polls.append(place)

print("The places than you like visit are: ")

for place in polls:
    print(place)