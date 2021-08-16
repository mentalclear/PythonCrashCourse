""" A function that accepts three parameters 
and returns a formatted string
"""
def formatted_city_country(city, country, population=0):
    if population > 0:
        return (f"{city.title()}, {country.title()} - population {population}")
    else:
        return (f"{city}, {country}").title()