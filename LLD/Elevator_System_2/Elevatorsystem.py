from enum import Enum
import heapq
import threading
import logging
from abc import ABC, abstractmethod

class Direction(Enum):
    UP = 1
    DOWN = 2

class ElevatorState(Enum):
    MOVING = 1
    IDLE = 2

class ElevatorDoor:
    def openDoor(self):
        print("Opening the Elevator door")

    def closeDoor(self):
        print("Closing the Elevator door")

class ElevatorCar:
    def __init__(self, id):
        self.id = id
        self.state = ElevatorState.IDLE
        self.currentFloor = 0
        self.direction = Direction.UP
        self.door = ElevatorDoor()

    def moveElevator(self, direction, floor):
        if direction == Direction.UP and floor <= self.currentFloor:
            raise ValueError("Cannot move up to a lower or same floor")
        if direction == Direction.DOWN and floor >= self.currentFloor:
            raise ValueError("Cannot move down to a higher or same floor")

        logging.info(f"Elevator {self.id} moving from floor {self.currentFloor} to floor {floor}")
        self.state = ElevatorState.MOVING
        self.direction = direction
        self.currentFloor = floor
        self.state = ElevatorState.IDLE

class InternalButtons:
    def __init__(self, controller):
        self.controller = controller

    def pressButton(self, floor):
        self.controller.submitInternalRequest(floor)

class ExternalButtons:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def pressButton(self, floor, direction):
        self.dispatcher.submitExternalRequest(floor, direction)

class DispatchStrategy(ABC):
    @abstractmethod
    def chooseElevator(self, elevators, floor, direction):
        pass

class NearestElevatorStrategy(DispatchStrategy):
    def chooseElevator(self, elevators, floor, direction):
        return min(elevators, key=lambda e: abs(e.elevatorCar.currentFloor - floor))

class EvenOddStrategy(DispatchStrategy):
    def chooseElevator(self, elevators, floor, direction):
        return next(e for e in elevators if e.elevatorCar.id % 2 == floor % 2)


class SmartDispatchStrategy(DispatchStrategy):
    def chooseElevator(self, elevators, floor, direction):
        # Filter elevators that are moving in the same direction as the request
        same_direction_elevators = [e for e in elevators if e.elevatorCar.direction == direction]

        if direction == Direction.UP:
            # If the request is to move up, choose among elevators that are below the requested floor
            candidate_elevators = [e for e in same_direction_elevators if e.elevatorCar.currentFloor <= floor]
        else:  # direction == Direction.DOWN
            # If the request is to move down, choose among elevators that are above the requested floor
            candidate_elevators = [e for e in same_direction_elevators if e.elevatorCar.currentFloor >= floor]

        if candidate_elevators:
            # If there are any candidate elevators, choose the nearest one
            return min(candidate_elevators, key=lambda e: abs(e.elevatorCar.currentFloor - floor))
        else:
            # If there are no candidate elevators, fall back to choosing the nearest elevator
            return min(elevators, key=lambda e: abs(e.elevatorCar.currentFloor - floor))



class ElevatorController:
    def __init__(self, elevatorCar, dispatchStrategy, numFloors):
        self.elevatorCar = elevatorCar
        self.requests = []
        self.lock = threading.Lock()
        self.dispatchStrategy = dispatchStrategy
        self.internalButtons = InternalButtons(self)

    def submitExternalRequest(self, floor, direction):
        with self.lock:
            heapq.heappush(self.requests, (floor, direction))

    def submitInternalRequest(self, floor):
        with self.lock:
            heapq.heappush(self.requests, (floor, self.elevatorCar.direction))

    def controlElevator(self):
        while True:
            with self.lock:
                if self.requests:
                    floor, direction = heapq.heappop(self.requests)
                    self.elevatorCar.moveElevator(direction, floor)

class ExternalDispatcher:
    def __init__(self, elevators, dispatchStrategy):
        self.elevators = elevators
        self.dispatchStrategy = dispatchStrategy

    def submitExternalRequest(self, floor, direction):
        elevator = self.dispatchStrategy.chooseElevator(self.elevators, floor, direction)
        elevator.submitExternalRequest(floor, direction)

class Building:
    def __init__(self, numFloors, numElevators, dispatchStrategy):
        self.elevators = [ElevatorController(ElevatorCar(i), dispatchStrategy, numFloors) for i in range(numElevators)]
        self.externalDispatcher = ExternalDispatcher(self.elevators, dispatchStrategy)
        self.floors = [Floor(i, self.externalDispatcher) for i in range(numFloors)]

    def addFloor(self, floor):
        self.floors.append(floor)

    def removeFloor(self, floor):
        self.floors.remove(floor)

    def getFloors(self):
        return self.floors

class Floor:
    def __init__(self, floorNumber, externalDispatcher):
        self.floorNumber = floorNumber
        self.externalButtons = ExternalButtons(externalDispatcher)

    def pressButton(self, direction):
        self.externalButtons.pressButton(self.floorNumber, direction)

def main():
    building = Building(10, 2, NearestElevatorStrategy())
    building.floors[0].pressButton(Direction.UP)
    for elevator in building.elevators:
        threading.Thread(target=elevator.controlElevator).start()

if __name__ == "__main__":
    main()
