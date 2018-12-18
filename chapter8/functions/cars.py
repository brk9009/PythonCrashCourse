# 8.13 Python Crash Course
def make_car(manufacturer, model_name, **features):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name
    for key, value in features.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', color='blue', towPackage=True)
print(car)
