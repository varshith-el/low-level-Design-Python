from abc import ABC, abstractmethod

# Abstract Product
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete Product 1
class Truck(Transport):
    def deliver(self):
        return "Delivery by road in a truck."

# Concrete Product 2
class Ship(Transport):
    def deliver(self):
        return "Delivery by sea in a ship."

# Abstract Factory
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

# Concrete Factory 1
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

# Concrete Factory 2
class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

# Abstract Factory for creating factories
class LogisticsFactory(ABC):
    @abstractmethod
    def create_logistics(self):
        pass

# Concrete Factory for creating RoadLogistics
class RoadLogisticsFactory(LogisticsFactory):
    def create_logistics(self):
        return RoadLogistics()

# Concrete Factory for creating SeaLogistics
class SeaLogisticsFactory(LogisticsFactory):
    def create_logistics(self):
        return SeaLogistics()

# Client code
def logistics_app(logistics_factory):
    logistics = logistics_factory.create_logistics()
    print(logistics.create_transport().deliver())

logistics_app(RoadLogisticsFactory())
logistics_app(SeaLogisticsFactory())





#below code has the factory method as well as abstract factory.

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Delivery by road in a truck."

class Ship(Transport):
    def deliver(self):
        return "Delivery by sea in a ship."

class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

class LogisticsFactory(ABC):
    @abstractmethod
    def create_logistics(self):
        pass

class RoadLogisticsFactory(LogisticsFactory):
    def create_logistics(self):
        return RoadLogistics()

class SeaLogisticsFactory(LogisticsFactory):
    def create_logistics(self):
        return SeaLogistics()

def logistics_app(logistics_factory):
    logistics = logistics_factory.create_logistics()
    print(logistics.create_transport().deliver())

logistics_app(RoadLogisticsFactory())
logistics_app(SeaLogisticsFactory())


