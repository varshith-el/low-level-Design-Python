# Strategy interface
class DriveStrategy:
    def drive(self, vehicle):
        raise NotImplementedError

# Concrete strategies
class RacingMode(DriveStrategy):
    def drive(self, vehicle):
        # implement the logic for racing mode
        # for example, increase the speed, enable turbo, etc.
        print(f"{vehicle.name} is driving in racing mode")

class OffRoadMode(DriveStrategy):
    def drive(self, vehicle):
        # implement the logic for off road mode
        # for example, adjust the suspension, enable 4x4, etc.
        print(f"{vehicle.name} is driving in off road mode")

class CruisingMode(DriveStrategy):
    def drive(self, vehicle):
        # implement the logic for cruising mode
        # for example, reduce the speed, enable eco mode, etc.
        print(f"{vehicle.name} is driving in cruising mode")

# Context interface
class Vehicle:
    def __init__(self, name, drive_strategy=None):
        self.name = name
        self.drive_strategy = drive_strategy or CruisingMode()

    def drive(self):
        self.drive_strategy.drive(self)

# Concrete contexts
class Sport(Vehicle):
    def __init__(self, name):
        super().__init__(name, RacingMode())

class SUV(Vehicle):
    def __init__(self, name):
        super().__init__(name, OffRoadMode())

class Hatchback(Vehicle):
    def __init__(self, name):
        super().__init__(name, CruisingMode())

# Usage example
s = Sport("Mazda")
s.drive() # prints Mazda is driving in racing mode

u = SUV("Tesla")
u.drive() # prints Tesla is driving in off road mode

h = Hatchback("Audi")
h.drive() # prints Audi is driving in cruising mode

# Change the drive strategy at runtime
h.drive_strategy = RacingMode()
h.drive() # prints Audi is driving in racing mode
