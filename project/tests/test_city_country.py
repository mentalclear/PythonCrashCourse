from chapter11.exercises.exercise11_2.city_functions import formatted_city_country

def test_city_country():
    """ Make sure that the function return exepcted fromat 
        inputs like: 'santiago', 'chile'
    """
    formatted_result = formatted_city_country('santiago', 'chile')
    assert formatted_result == 'Santiago, Chile'

def test_city_country_population():
    """ Make sure that the function return expected fromat 
        inputs like: 'santiago', 'chile', 5000000
    """
    formatted_result = formatted_city_country('santiago', 'chile', 5000000)
    assert formatted_result == 'Santiago, Chile - population 5000000'    
