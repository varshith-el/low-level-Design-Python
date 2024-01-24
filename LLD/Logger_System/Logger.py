
"""
Logger System using Chain of Responsibility Pattern

"""

from abc import ABC, abstractmethod

#Abstract Class
class AbstractLogger(ABC):
    TRACE = 1
    INFO = 2
    DEBUG = 3
    WARNING = 4
    ERROR = 5

    def __init__(self, level):
        self.next_logger = None
        self.level = level

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger

    def log_message(self, level, message):
        if self.level <= level:
            self.write(message)
        if self.next_logger is not None:
            self.next_logger.log_message(level, message)

    @abstractmethod
    def write(self, message):
        pass

#Concrete Class
class ConsoleLogger(AbstractLogger):
    def write(self, message):
        print(f"Standard Console::Logger: {message}")

#Concrete Class
class ErrorLogger(AbstractLogger):
    def write(self, message):
        print(f"Error Console::Logger: {message}")

#Concrete Class
class FileLogger(AbstractLogger):
    def write(self, message):
        print(f"File::Logger: {message}")

#Client
error_logger = ErrorLogger(AbstractLogger.ERROR)
file_logger = FileLogger(AbstractLogger.DEBUG)
console_logger = ConsoleLogger(AbstractLogger.INFO)

error_logger.set_next_logger(file_logger)
file_logger.set_next_logger(console_logger)

logger_chain = error_logger
logger_chain.log_message(AbstractLogger.INFO, "This is an information.")
logger_chain.log_message(AbstractLogger.DEBUG, "This is a debug level information.")
logger_chain.log_message(AbstractLogger.ERROR, "This is an error information.")
