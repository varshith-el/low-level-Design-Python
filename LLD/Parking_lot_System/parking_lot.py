from abc import ABC, abstractmethod
from enum import Enum
import time

class VehicleType(Enum):
    TWO_WHEELER = 1
    FOUR_WHEELER = 2

# vehicle object
class Vehicle:
    def __init__(self, vehicle_no, vehicle_type):
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type

# parking spot interface, define the parking spot
class ParkingSpot(ABC):
    def __init__(self, id, price):
        self.id = id
        self.is_empty = True
        self.vehicle = None
        self.price = price

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_empty = False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_empty = True

#concrete praking spot class
class TwoWheelerSpot(ParkingSpot):
    def __init__(self, id):
        super().__init__(id, 10)

#concrete praking spot class
class FourWheelerSpot(ParkingSpot):
    def __init__(self, id):
        super().__init__(id, 20)



class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, list):
        pass

class NearToEntrance(ParkingStrategy):
    def find_parking_spot(self, list):
        # Assuming the list is sorted by distance to the entrance
        for spot in list:
            if spot.is_empty:
                return spot
        return None

class NearToEntranceAndElevator(ParkingStrategy):
    def find_parking_spot(self, list):
        # Assuming the list is sorted by distance to the entrance and elevator
        for spot in list:
            if spot.is_empty:
                return spot
        return None



# we need a parking spot manager to listout/maintain all the parking spots.
#initialised with list of parking sopt objs and the parking strategy for type of vehicle, is has park vehicle, remove vehicle, add the spot to list and similarly remove a spot.
class ParkingSpotManager(ABC):
    def __init__(self, list, parking_strategy):
        self.list = list
        self.parking_strategy = parking_strategy or NearToEntrance()

    def find_parking_space(self):
        return self.parking_strategy.find_parking_spot(self.list)

    def add_parking_space(self, spot):
        self.list.append(spot)

    def remove_parking_space(self, spot):
        self.list.remove(spot)

    #park the given vehicle in a spot.
    def park_vehicle(self, vehicle):
        spot = self.find_parking_space()
        if spot is not None:
            spot.assign_vehicle(vehicle)
        return spot
    #remove the given vehicle from the spot 
    def remove_vehicle(self, vehicle):
        for spot in self.list:
            if spot.vehicle == vehicle:
                spot.remove_vehicle()
                return True
        return False
    
#concrete ParkingSpotManager classes passes the list and parking strategy.
class TwoWheelerManager(ParkingSpotManager):
    def __init__(self, list):
        super().__init__(list, NearToEntrance())

#concrete ParkingSpotManager classes
class FourWheelerManager(ParkingSpotManager):
    def __init__(self, list):
        super().__init__(list, NearToEntranceAndElevator())

#Based on the vehicle type, get the appropriate vehiclemanager using factory pattern
class ParkingSpotManagerFactory:
    def get_parking_spot_manager(self, vehicle):
        if vehicle.vehicle_type == VehicleType.TWO_WHEELER:
            return TwoWheelerManager([]) # initiate a twowheeler obj
        elif vehicle.vehicle_type == VehicleType.FOUR_WHEELER:
            return FourWheelerManager([])
        else:
            return None

#ticket obj, has entry time, vehicle obj, and the parking spot.
class Ticket:
    def __init__(self, vehicle, parking_spot):
        self.entry_time = time.time()
        self.vehicle = vehicle
        self.parking_spot = parking_spot

# entrance gate has factory of ParkingSpotManagerFactory, parking space manager, 
class EntranceGate:
    def __init__(self):
        self.factory = ParkingSpotManagerFactory()
        self.parking_space_manager = None
        self.ticket = None

    #retrive the parking spot by vehicle type.
    def find_parking_space(self, vehicle):
        self.parking_space_manager = self.factory.get_parking_spot_manager(vehicle)
        return self.parking_space_manager.find_parking_space()
    
    #book the spot 
    def book_spot(self, vehicle):
        spot = self.find_parking_space(vehicle)
        if spot is not None:
            self.parking_space_manager.park_vehicle(vehicle)
        return spot
    #generate the ticket for the spot
    def generate_ticket(self, vehicle, parking_spot):
        self.ticket = Ticket(vehicle, parking_spot)
        return self.ticket

class CostComputationFactory:
    def get_cost_computation(self, ticket):
        if ticket.vehicle.vehicle_type == VehicleType.TWO_WHEELER:
            return TwoWheelerCostComputation()
        elif ticket.vehicle.vehicle_type == VehicleType.FOUR_WHEELER:
            return FourWheelerCostComputation()
        else:
            return None


#Pricing Strategy
class PricingStrategy(ABC):
    @abstractmethod
    def price(self, ticket):
        pass

class Hourly(PricingStrategy):
    def price(self, ticket):
        hours = (time.time() - ticket.entry_time) // 3600
        return hours * ticket.parking_spot.price

class MinuteBasis(PricingStrategy):
    def price(self, ticket):
        minutes = (time.time() - ticket.entry_time) // 60
        return minutes * ticket.parking_spot.price

#Compute the Cost
class CostComputation(ABC):
    def __init__(self, pricing_strategy):
        self.pricing_strategy = pricing_strategy

    def price(self, ticket):
        return self.pricing_strategy.price(ticket)

class TwoWheelerCostComputation(CostComputation):
    def __init__(self):
        super().__init__(Hourly())

class FourWheelerCostComputation(CostComputation):
    def __init__(self):
        super().__init__(MinuteBasis())


#make payment
class PaymentStrategy(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class Card(PaymentStrategy):
    def make_payment(self, amount):
        # save in card table
        pass

class Cash(PaymentStrategy):
    def make_payment(self, amount):
        # save in cash table
        pass


#Payment Strategy
class Payment(ABC):
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount):
        return self.payment_strategy.make_payment(amount)

class CardPayment(Payment):
    def __init__(self):
        super().__init__(Card())

class CashPayment(Payment):
    def __init__(self):
        super().__init__(Cash())

#Payment Factory
class PaymentFactory:
    def get_payment(self, payment_method):
        if payment_method == "Cash":
            return CashPayment()
        elif payment_method == "Card":
            return CardPayment()
        else:
            return None


class ExitGate:
    def __init__(self, payment_method, parking_spot_manager_factory, ticket, cost_computation_factory, payment_factory):
        self.payment_method = payment_method
        self.parking_spot_manager_factory = parking_spot_manager_factory
        self.ticket = ticket
        self.cost_computation_factory = cost_computation_factory
        self.payment_factory = payment_factory

    def price_calculation(self):
        amount = self.cost_computation_factory.get_cost_computation(self.ticket).price(self.ticket)
        return amount

    def make_payment(self):
        amount = self.price_calculation()
        return self.payment_factory.get_payment(self.payment_method).make_payment(amount)

    def remove_vehicle(self):
        self.parking_spot_manager_factory.get_parking_spot_manager(self.ticket.vehicle).remove_vehicle(self.ticket.vehicle)
