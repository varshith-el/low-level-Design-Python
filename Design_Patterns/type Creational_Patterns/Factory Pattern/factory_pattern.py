from abc import ABC, abstractmethod

#Abstract baase Product Interface
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete Product Truck
class Truck(Transport):
    def deliver(self):
        return "Delivery by road in a truck."

#Concrete Product Ship
class Ship(Transport):
    def deliver(self):
        return "Delivery by sea in a ship."

#Abstract base Creator class
class Logistics(ABC):
    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()

    @abstractmethod
    def create_transport(self):
        pass

#Concrete Creator Road Logistics
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()
    
#Concrete Creator Sea Logistics
class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


def logistics_app(logistics_type):
    if logistics_type == "Road":
        logistics = RoadLogistics()
    elif logistics_type == "Sea":
        logistics = SeaLogistics()
    else:
        raise ValueError("Invalid logistics type")
    print(logistics.plan_delivery())



#client code
logistics_app("Road")
logistics_app("Sea")



"""
=> Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.

=> Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.

=> Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.
"""