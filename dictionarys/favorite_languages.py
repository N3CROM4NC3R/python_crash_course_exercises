favoriteLanguages={
    "jen"       : "python",
    "sarah"     : "c",
    "edward"    : "ruby",
    "phil"      : "python",
    "eneimar"    : "",
    "sebastian" : ""}

for key,value in favoriteLanguages.items():
    if value:
        print("thanking them for responding,",key.title(),",Your favorite language is:",value.title(p))
    else:
        print("I invite you to take the poll,",key.title())
