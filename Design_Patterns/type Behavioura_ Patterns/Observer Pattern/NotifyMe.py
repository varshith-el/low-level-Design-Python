# Define an abstract observer class that has an update method
class Observer:
    def update(self, subject):
        pass

# Define a concrete observer class that sends email notifications
#Notice here we pass the concrete Subject in the update.
class EmailObserver(Observer):
    def __init__(self, email):
        self.email = email # Store the email address of the observer
    
    def update(self, subject):
        # Send an email to the observer with the subject's state
        print(f"Sending email to {self.email} with message: {subject.get_state()}")

# Define a concrete observer class that sends SMS notifications
class SMSObserver(Observer):
    def __init__(self, phone):
        self.phone = phone # Store the phone number of the observer
    
    def update(self, subject):
        # Send an SMS to the observer with the subject's state
        print(f"Sending SMS to {self.phone} with message: {subject.get_state()}")

# Define an abstract subject class that has a list of observers and methods to attach, detach and notify them
class Subject:
    def __init__(self):
        self.observers = [] # Create an empty list of observers
    
    def attach(self, observer):
        # Add an observer to the list if it is not already there
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        # Remove an observer from the list if it is there
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self):
        # Call the update method of each observer with self as the argument
        for observer in self.observers:
            observer.update(self)
    
    def get_state(self):
        # Return the state of the subject
        pass
    
    def set_state(self, state):
        # Set the state of the subject and notify the observers
        pass

# Define a concrete subject class that represents a mobile phone store
class MobileStore(Subject):
    def __init__(self, model):
        super().__init__() # Call the parent class constructor
        self.model = model # Store the model name of the mobile phone
        self.available = False # Store the availability status of the mobile phone
    
    def get_state(self):
        # Return a message with the model name and availability status
        if self.available:
            return f"The mobile phone {self.model} is now available in our store."
        else:
            return f"The mobile phone {self.model} is currently out of stock."
    
    def set_state(self, available):
        # Set the availability status and notify the observers
        self.available = available
        self.notify()
    
    #You can use below usecase too.but make sure to create stockCount in the constructor.
    
    def set_state(self,newStockCount):
        self.available = True
        if stockCount == 0:
            self.notify()
        stockCount += newStockCount

    '''
    def notify(self):
        
    '''

# Define a concrete subject class that represents a course website
class CourseWebsite(Subject):
    def __init__(self, name):
        super().__init__() # Call the parent class constructor
        self.name = name # Store the name of the course
        self.assignment = None # Store the name of the current assignment
    
    def get_state(self):
        # Return a message with the course name and assignment name
        if self.assignment:
            return f"A new assignment {self.assignment} has been posted on the course website {self.name}."
        else:
            return f"There is no new assignment on the course website {self.name}."
    
    def set_state(self, assignment):
        # Set the assignment name and notify the observers
        self.assignment = assignment
        self.notify()

# Create a mobile store object with a model name
mobile_store = MobileStore("iPhone 13")

# Create some email and SMS observers with their contact details
email_observer_1 = EmailObserver("alice@example.com")
email_observer_2 = EmailObserver("bob@example.com")
sms_observer_1 = SMSObserver("111-111-1111")
sms_observer_2 = SMSObserver("222-222-2222")

# Attach the observers to the mobile store subject
mobile_store.attach(email_observer_1)
mobile_store.attach(email_observer_2)
mobile_store.attach(sms_observer_1)
mobile_store.attach(sms_observer_2)

# Change the state of the mobile store subject to True
mobile_store.set_state(True)

# Output:
# Sending email to alice@example.com with message: The mobile phone iPhone 13 is now available in our store.
# Sending email to bob@example.com with message: The mobile phone iPhone 13 is now available in our store.
# Sending SMS to 111-111-1111 with message: The mobile phone iPhone 13 is now available in our store.
# Sending SMS to 222-222-2222 with message: The mobile phone iPhone 13 is now available in our store.

# Detach some observers from the mobile store subject
mobile_store.detach(email_observer_2)
mobile_store.detach(sms_observer_2)

# Change the state of the mobile store subject to False
mobile_store.set_state(False)

# Output:
# Sending email to alice@example.com with message: The mobile phone iPhone 13 is currently out of stock.
# Sending SMS to 111-111-1111 with message: The mobile phone iPhone 13 is currently out of stock.

# Create a course website object with a name
course_website = CourseWebsite("Python Programming")

# Attach some observers to the course website subject
course_website.attach(email_observer_1)
course_website.attach(sms_observer_2)

# Change the state of the course website subject to a new assignment name
course_website.set_state("Assignment 1")

# Output:
# Sending email to alice@example.com with message: A new assignment Assignment 1 has been posted on the course website Python Programming.
# Sending SMS to 222-222-2222 with message: A new assignment Assignment 1 has been posted on the course website Python Programming.

# Change the state of the course website subject to another new assignment name
course_website.set_state("Assignment 2")

# Output:
# Sending email to alice@example.com with message: A new assignment Assignment 2 has been posted on the course website Python Programming.
# Sending SMS to 222-222-2222 with message: A new assignment Assignment 2 has been posted on the course website Python Programming.

################################################################
# Define a concrete observer class that stores the mobile store object
class EmailObserver(Observer):
    def __init__(self, mobile_store, email):
        self._mobile_store = mobile_store # Store the mobile store object, we can pass any subject that can be observed.
        self._email = email # Store the email address of the customer
        self._mobile_store.attach(self) # Register with the mobile store
    
    def __del__(self):
        self._mobile_store.detach(self) # Unregister from the mobile store
        self._mobile_store = None # Remove the reference to the mobile store
    
    def update(self):
        # Get the state from the mobile store object
        message = self._mobile_store.get_state()
        # Send an email to the customer with the message
        print(f"Sending email to {self._email} with message: {message}")
