def make_car(maker, model, **options):
    """ Building a dictionary for a car """    
    car_info = {
        'manufacturer' : maker.title(),
        'model': model.title()        
    }
    
    for option, value in options.items():
        car_info[option] = value

    return car_info

car = make_car('subaru', 'outback', color='blue', gearbox='auto')
print(car)

print(make_car('toyota', 'camry'))
