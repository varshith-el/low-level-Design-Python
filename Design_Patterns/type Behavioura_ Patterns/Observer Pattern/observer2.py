# Define an abstract observer class that has an update method
class Observer:
    def update(self, subject):
        pass

# Define a concrete observer class that sends email notifications
class EmailObserver(Observer):
    def __init__(self, email):
        self.email = email # Store the email address of the observer
    
    def update(self, subject):
        # Send an email to the observer with the subject's state
        print(f"Sending email to {self.email} with message: {subject.get_state()}")

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

# Define a concrete subject class that represents the iPhone stock availability in Amazon.com
class AmazonStock(Subject):
    def __init__(self, model, url):
        super().__init__() # Call the parent class constructor
        self.model = model # Store the model name of the iPhone
        self.url = url # Store the URL of the product page
        self.available = False # Store the availability status of the iPhone
    
    def get_state(self):
        # Return a message with the model name, URL and availability status
        if self.available:
            return f"The iPhone {self.model} is now available in Amazon.com. You can buy it from this link: {self.url}"
        else:
            return f"The iPhone {self.model} is currently out of stock in Amazon.com. Please check again later."
    
    def set_state(self, available):
        # Set the availability status and notify the observers
        self.available = available
        self.notify()


def main():
    # Create an Amazon stock object with a model name and a URL
    amazon_stock = AmazonStock("13", "[1](https://www.amazon.in/Apple-iPhone-13-128GB-Product/dp/B09G99CW2N)")

    # Create some email observers with their email addresses
    email_observer_1 = EmailObserver("alice@example.com")
    email_observer_2 = EmailObserver("bob@example.com")

    # Attach the observers to the Amazon stock subject
    amazon_stock.attach(email_observer_1)
    amazon_stock.attach(email_observer_2)

    # Change the state of the Amazon stock subject to True
    amazon_stock.set_state(True)

    # Output:
    # Sending email to alice@example.com with message: The iPhone 13 is now available in Amazon.com. You can buy it from this link: [1](https://www.amazon.in/Apple-iPhone-13-128GB-Product/dp/B09G99CW2N)
    # Sending email to bob@example.com with message: The iPhone 13 is now available in Amazon.com. You can buy it from this link: [1](https://www.amazon.in/Apple-iPhone-13-128GB-Product/dp/B09G99CW2N)

    # Detach an observer from the Amazon stock subject
    amazon_stock.detach(email_observer_2)

    # Change the state of the Amazon stock subject to False
    amazon_stock.set_state(False)

    # Output:
    # Sending email to alice@example.com with message: The iPhone 13 is currently out of stock in Amazon.com. Please check again later.




if __name__ == "__main__":
    main()