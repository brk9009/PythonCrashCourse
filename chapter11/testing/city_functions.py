#11.1 Python Crash Course

def get_city_country(city, country, population=''):
    """Returns a city and country"""
    if population:
        city_country = city + ', ' + country + ' - ' + population
    else:
        city_country = city + ', ' + country
    return city_country.title()
