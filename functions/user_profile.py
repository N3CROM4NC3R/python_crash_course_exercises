def build_profile(first_name,last_name,**information):
    profile = {
        "first_name" : first_name,
        "last_name" : last_name
    }
    for key,value in information.items():
        profile[key] = value

    return profile

profile = build_profile(first_name="Santiago",last_name="Padròn",location="Valle de la pascua",
                        ocupation="student")
for key,value in profile.items():
    print(key," => ",value)