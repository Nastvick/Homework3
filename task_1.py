class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        return f'{self.brand} is moving!'


class Bus(Vehicle):
    def _move(self):
        return f'{self.brand} is moving!'


chevrolet_camaro = Vehicle("Chevrolet Camaro", 1977, 240)
concorde = Vehicle("Concorde", 1965, 2179)
hms_defender = Vehicle("HMS Defender", 2006, 59)

some_bus = Bus("BMW", 2008, 70)


print(chevrolet_camaro.move())
print(concorde.move())
print(hms_defender.move())
print(some_bus.move())



