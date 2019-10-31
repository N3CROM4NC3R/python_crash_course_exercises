def city_country(city_name,country_name,population=''):
    if population:
        location = city_name + ', ' + country_name + ' - ' + population
    else:
        location = city_name + ', ' + country_name

    return location.title()

