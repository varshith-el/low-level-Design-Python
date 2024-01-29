from abc import ABC, abstractmethod

# This is our abstract class which both Document and ProxyDocument will implement
class AbstractDocument(ABC):
    @abstractmethod
    def display(self):
        pass

# This is our real class which will be accessed through proxy
class Document(AbstractDocument):
    def __init__(self, filename):
        self._filename = filename
        print(f"Loading document {self._filename}")

    def display(self):
        print(f"Displaying document {self._filename}")

# This is our proxy class which will control access to Document
class ProxyDocument(AbstractDocument):
    def __init__(self, filename):
        self._filename = filename
        self._document = None

    def display(self):
        if self._document is None:
            self._document = Document(self._filename)
        self._document.display()

# Using the ProxyDocument
proxy = ProxyDocument("test_doc")
# Document is not loaded until required
proxy.display()  # Document is loaded and displayed
proxy.display()  # Document is now displayed without loading




"""
from abc import ABC, abstractmethod

# This is our abstract class which both Document and ProxyDocument will implement
class AbstractDocument(ABC):
    @abstractmethod
    def display(self):
        pass

# This is our real class which will be accessed through proxy
class Document(AbstractDocument):
    def __init__(self, filename):
        self._filename = filename
        print(f"Loading document {self._filename}")

    def display(self):
        print(f"Displaying document {self._filename}")

# This is our proxy class which will control access to Document
class ProxyDocument(AbstractDocument):
    def __init__(self, filename):
        self._filename = filename
        self._document = None

    def display(self):
        if self._document is None:
            self._document = Document(self._filename)
        self._document.display()

# Using the ProxyDocument
proxy = ProxyDocument("test_doc")
# Document is not loaded until required
proxy.display()  # Document is loaded and displayed
proxy.display()  # Document is now displayed without loading

"""