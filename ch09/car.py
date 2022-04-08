class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.tank = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        self.odometer = mileage

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def fill_gas_tank(self):
        print(f"This car has {self.tank} tank.")


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer = 23
my_new_car.read_odometer()
my_new_car.update_odometer(43)
my_new_car.read_odometer()
my_new_car.tank = 60
my_new_car.fill_gas_tank()