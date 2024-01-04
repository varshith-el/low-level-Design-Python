from elevator.main import Elevator

class ElevatorSystem:
    """
    ElevatorSystem - Class that contains array of Elevator objects
    self.number_of_lifts = total number of lifts in the system
    self.floor_max = top floor
    self.floor_min = bottom most floor
    self.request_queue = request queue for each lift

    """

    def __init__(self, number_of_lifts, floor_min, floor_max,request_each, lift_positions=[]):
        self.number_of_lifts = number_of_lifts
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.elevators = []
        self.request_queue = request_each

        # safegaurd in case no initial positining of lift is given
        # all start from 0 in that case.
        if len(lift_positions) < 0:
            lift_positions = [0] * number_of_lifts

        # create an array of elevator objects
        for each in range(0, number_of_lifts):
            new_elevator = Elevator(each, floor_min, floor_max,lift_positions[each])
            self.elevators.append(new_elevator)



        '''
#factory pattern
class ElevatorFactory:
    def create_elevator(self, type, *args, **kwargs):
        if type == 'StandardElevator':
            return StandardElevator(*args, **kwargs)
        elif type == 'ExpressElevator':
            return ExpressElevator(*args, **kwargs)
        else:
            raise ValueError('Invalid elevator type')


# create an instance of ElevatorFactory
factory = ElevatorFactory()

# create an array of elevator objects
for each in range(0, number_of_lifts):
    # determine the type of elevator to create
    type = 'StandardElevator' if each % 2 == 0 else 'ExpressElevator'
    
    # create the elevator using the factory
    new_elevator = factory.create_elevator(type, each, floor_min, floor_max, lift_positions[each])
    
    self.elevators.append(new_elevator)
        '''
        #DIP principle
'''
from abc import ABC, abstractmethod

class AbstractElevator(ABC):
    @abstractmethod
    def move_one_step(self):
        pass

    @abstractmethod
    def execute_request(self, list_of_request):
        pass

class Elevator(AbstractElevator):
    # ... existing Elevator code ...

class ExpressElevator(AbstractElevator):
    # ... ExpressElevator code ...

class ElevatorSystem:
    def __init__(self, number_of_lifts, floor_min, floor_max,request_each, lift_positions=[]):
        self.number_of_lifts = number_of_lifts
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.elevators = []
        self.request_queue = request_each

        # create an array of elevator objects
        for each in range(0, number_of_lifts):
            if each % 2 == 0:
                new_elevator = Elevator(each, floor_min, floor_max,lift_positions[each])
            else:
                new_elevator = ExpressElevator(each, floor_min, floor_max,lift_positions[each])
            self.elevators.append(new_elevator)

The ElevatorSystem class is dependent on the Elevator class because it creates instances of Elevator and calls methods on these instances. This means that if you wanted to change the behavior of the elevators (for example, to create different types of elevators or to change how an elevator moves), you would need to modify the Elevator class, and this could potentially affect the ElevatorSystem class.

By applying the Dependency Inversion Principle (DIP), you can make the ElevatorSystem class depend on an AbstractElevator interface (or abstract base class in Python) instead of the concrete Elevator class. This way, the ElevatorSystem class is insulated from changes to the Elevator class, and you can easily introduce new types of elevators by creating new classes that implement the AbstractElevator interface. This makes the code more flexible and easier to maintain. 😊

    '''

from elevator_system.helpers.process import process_request
