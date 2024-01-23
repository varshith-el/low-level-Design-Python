
from enum import Enum
from datetime import date

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2


class VehicleType(Enum):
    CAR = 1
    BIKE = 2


class Vehicle:
    def __init__(self):
        self.vehicleID = None
        self.vehicleNumber = None
        self.vehicleType = None
        self.companyName = None
        self.modelName = None
        self.kmDriven = None
        self.manufacturingDate = None
        self.average = None
        self.cc = None
        self.dailyRentalCost = None
        self.hourlyRentalCost = None
        self.noOfSeat = None
        self.status = None

    # getters and setters
    def get_vehicleID(self):
        return self.vehicleID

    def set_vehicleID(self, vehicleID):
        self.vehicleID = vehicleID

    def get_vehicleNumber(self):
        return self.vehicleNumber

    def set_vehicleNumber(self, vehicleNumber):
        self.vehicleNumber = vehicleNumber

    def get_vehicleType(self):
        return self.vehicleType

    def set_vehicleType(self, vehicleType):
        self.vehicleType = vehicleType

    def get_companyName(self):
        return self.companyName

    def set_companyName(self, companyName):
        self.companyName = companyName

    def get_modelName(self):
        return self.modelName

    def set_modelName(self, modelName):
        self.modelName = modelName

    def get_kmDriven(self):
        return self.kmDriven

    def set_kmDriven(self, kmDriven):
        self.kmDriven = kmDriven

    def get_manufacturingDate(self):
        return self.manufacturingDate

    def set_manufacturingDate(self, manufacturingDate):
        self.manufacturingDate = manufacturingDate

    def get_average(self):
        return self.average

    def set_average(self, average):
        self.average = average

    def get_cc(self):
        return self.cc

    def set_cc(self, cc):
        self.cc = cc

    def get_dailyRentalCost(self):
        return self.dailyRentalCost

    def set_dailyRentalCost(self, dailyRentalCost):
        self.dailyRentalCost = dailyRentalCost

    def get_hourlyRentalCost(self):
        return self.hourlyRentalCost

    def set_hourlyRentalCost(self, hourlyRentalCost):
        self.hourlyRentalCost = hourlyRentalCost

    def get_noOfSeat(self):
        return self.noOfSeat

    def set_noOfSeat(self, noOfSeat):
        self.noOfSeat = noOfSeat

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status



class Bike(Vehicle):
    pass

class Car(Vehicle):
    pass




class Bill:
    def __init__(self, reservation):
        self.reservation = reservation
        self.totalBillAmount = self.computeBillAmount()
        self.isBillPaid = False

    def computeBillAmount(self):
        return 100.0


class Location:
    def __init__(self, pincode, city, state, country):
        self.pincode = pincode
        self.city = city
        self.state = state
        self.country = country


class Payment:
    def payBill(self, bill):
        # do payment processing and update the bill status
        pass



class PaymentDetails:
    def __init__(self):
        self.paymentId = None
        self.amountPaid = None
        self.dateOfPayment = None
        self.isRefundable = None
        self.paymentMode = None


from enum import Enum

class PaymentMode(Enum):
    CASH = 1
    ONLINE = 2


from datetime import date

class Reservation:
    def __init__(self):
        self.reservationId = None
        self.user = None
        self.vehicle = None
        self.bookingDate = None
        self.dateBookedFrom = None
        self.dateBookedTo = None
        self.fromTimeStamp = None
        self.toTimeStamp = None
        self.pickUpLocation = None
        self.dropLocation = None
        self.reservationType = None
        self.reservationStatus = None
        self.location = None

    def createReserve(self, user, vehicle):
        # generate new id
        self.reservationId = 12232
        self.user = user
        self.vehicle = vehicle
        self.reservationType = ReservationType.DAILY
        self.reservationStatus = ReservationStatus.SCHEDULED

        return self.reservationId

    # CRUD operations




class ReservationStatus(Enum):
    SCHEDULED = 1
    INPROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4


class ReservationType(Enum):
    HOURLY = 1
    DAILY = 2


class Store:
    def __init__(self):
        self.storeId = None
        self.inventoryManagement = None
        self.storeLocation = None
        self.reservations = []

    def getVehicles(self, vehicleType):
        return self.inventoryManagement.getVehicles()

    # addVehicles, update vehicles, use inventory management to update those.

    def setVehicles(self, vehicles):
        self.inventoryManagement = VehicleInventoryManagement(vehicles)

    def createReservation(self, vehicle, user):
        reservation = Reservation()
        reservation.createReserve(user, vehicle)
        self.reservations.append(reservation)
        return reservation

    def completeReservation(self, reservationID):
        # take out the reservation from the list and call complete the reservation method.
        return True

    # update reservation


class User:
    def __init__(self):
        self.userId = None
        self.userName = None
        self.drivingLicense = None

    def get_userId(self):
        return self.userId

    def set_userId(self, userId):
        self.userId = userId

    def get_userName(self):
        return self.userName

    def set_userName(self, userName):
        self.userName = userName

    def get_drivingLicense(self):
        return self.drivingLicense

    def set_drivingLicense(self, drivingLicense):
        self.drivingLicense = drivingLicense



class VehicleInventoryManagement:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def getVehicles(self):
        # filtering
        return self.vehicles

    def setVehicles(self, vehicles):
        self.vehicles = vehicles



class VehicleRentalSystem:
    def __init__(self, stores, users):
        self.storeList = stores
        self.userList = users

    def getStore(self, location):
        # based on location, we will filter out the Store from storeList.
        return self.storeList[0]

    # addUsers

    # remove users

    # add stores

    # remove stores




class Main:
    @staticmethod
    def main():
        users = Main.addUsers()
        vehicles = Main.addVehicles()
        stores = Main.addStores(vehicles)

        rentalSystem = VehicleRentalSystem(stores, users)

        # 0. User comes
        user = users[0]

        # 1. user search store based on location
        location = Location(403012, "Bangalore", "Karnataka", "India")
        store = rentalSystem.getStore(location)

        # 2. get All vehicles you are interested in (based upon different filters)
        storeVehicles = store.getVehicles(VehicleType.CAR)

        # 3.reserving the particular vehicle
        reservation = store.createReservation(storeVehicles[0], users[0])

        # 4. generate the bill
        bill = Bill(reservation)

        # 5. make payment
        payment = Payment()
        payment.payBill(bill)

        # 6. trip completed, submit the vehicle and close the reservation
        store.completeReservation(reservation.reservationId)

    @staticmethod
    def addVehicles():
        vehicles = []

        vehicle1 = Car()
        vehicle1.set_vehicleID(1)
        vehicle1.set_vehicleType(VehicleType.CAR)

        vehicle2 = Car()
        vehicle2.set_vehicleID(2)
        vehicle2.set_vehicleType(VehicleType.CAR)

        vehicles.append(vehicle1)
        vehicles.append(vehicle2)

        return vehicles

    @staticmethod
    def addUsers():
        users = []
        user1 = User()
        user1.set_userId(1)

        users.append(user1)
        return users

    @staticmethod
    def addStores(vehicles):
        stores = []
        store1 = Store()
        store1.storeId = 1
        store1.set_vehicles(vehicles)

        stores.append(store1)
        return stores


if __name__ == "__main__":
    Main.main()
