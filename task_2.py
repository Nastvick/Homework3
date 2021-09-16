class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.name = name

    def move(self):
        return f'{self.name} is moving!'


class Bus(Vehicle):
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        return f'{self.__class__} is moving!'

    def __str__(self):
        return "Brand: {}, year_of_production: {}, max_speed: {}".format(self.brand, self.year_of_production,self.max_speed)

bus = Bus("School Bus", 1939, 70)

print(bus.move())
print(bus)
#не пойму как прописать, чтобы чтобы "Bus is moving!"
#я, кажется, в первом упражнении сделала несколько вариантов.