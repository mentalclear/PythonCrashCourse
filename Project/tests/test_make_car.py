from chapter8.exercises.exercise8_14 import *

maker = 'subaru'
model = 'outback'
test_dict = {
    'color' : 'blue',
    'touring_package' : True
}

def test_make_car_func():
    result = make_car(maker, model, color=test_dict['color'], touring_package=test_dict['touring_package'])
    assert result['manufacturer'] == 'Subaru'
    assert result['model'] == 'Outback'
    assert result['color'] == 'blue'
    assert result['touring_package'] == True