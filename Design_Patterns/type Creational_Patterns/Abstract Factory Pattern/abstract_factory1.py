from abc import ABC, abstractmethod

# Abstract product families
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Concrete product families
class WindowsButton(Button):
    def click(self):
        return "Windows Button clicked."

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox checked."

class MacButton(Button):
    def click(self):
        return "Mac Button clicked."

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac Checkbox checked."

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createCheckbox(self):
        pass

# Concrete factories
class WindowsFactory(GUIFactory):
    def createButton(self):
        return WindowsButton()

    def createCheckbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def createButton(self):
        return MacButton()

    def createCheckbox(self):
        return MacCheckbox()

# Client code
def client_code(factory: GUIFactory):
    button = factory.createButton()
    checkbox = factory.createCheckbox()

    print(button.click())
    print(checkbox.check())

# Using the client code
client_code(WindowsFactory())
client_code(MacFactory())


"""
Use the Abstract Factory when your code needs to work with various families of 


Consider implementing the Abstract Factory when you have a class with a set of Factory Methods that blur its primary responsibility.
"""

