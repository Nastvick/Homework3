class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.name = name

    def move(self):
        return f'{self.name} is moving!'


class Car(Vehicle):
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed


    def move(self):
        return f'{self.brand} is moving!'

    def __str__(self):
        return "Brand: {}, year_of_production: {}, max_speed: {}" .format(self.brand, self.year_of_production, self.max_speed)

class Plane(Vehicle):
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed


    def move(self):
        return f'{self.brand} is moving!'

    def __str__(self):
        return "Brand: {}, year_of_production: {}, max_speed: {}" .format(self.brand, self.year_of_production, self.max_speed)

class Ship(Vehicle):
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed


    def move(self):
        return f'{self.brand} is moving!'

    def __str__(self):
        return "Brand: {}, year_of_production: {}, max_speed: {}" .format(self.brand, self.year_of_production, self.max_speed)



chevrolet_camaro = Car("Chevrolet Camaro", 1977, 240)
concorde = Plane("Concorde", 1965, 2179)
hms_defender = Ship("HMS Defender", 2006, 59)


print(chevrolet_camaro.move())
print(chevrolet_camaro)
print(concorde.move())
print(concorde)
print(hms_defender.move())
print(hms_defender)

