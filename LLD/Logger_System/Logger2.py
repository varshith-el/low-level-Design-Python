"""
Logger system using Factory method.
"""


from abc import ABC, abstractmethod
from enum import Enum

class LogLevel(Enum):
    TRACE = 1
    INFO = 2
    DEBUG = 3
    WARNING = 4
    ERROR = 5

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class TraceLogger(Logger):
    def log(self, message: str) -> None:
        print(f"TRACE: {message}")

class InfoLogger(Logger):
    def log(self, message: str) -> None:
        print(f"INFO: {message}")

class DebugLogger(Logger):
    def log(self, message: str) -> None:
        print(f"DEBUG: {message}")

class WarningLogger(Logger):
    def log(self, message: str) -> None:
        print(f"WARNING: {message}")

class ErrorLogger(Logger):
    def log(self, message: str) -> None:
        print(f"ERROR: {message}")

class LoggerFactory:
    _loggers = {}

    @staticmethod
    def get_logger(level: LogLevel) -> Logger:
        if level not in LoggerFactory._loggers:
            if level == LogLevel.TRACE:
                LoggerFactory._loggers[LogLevel.TRACE] = TraceLogger()
            elif level == LogLevel.INFO:
                LoggerFactory._loggers[LogLevel.INFO] = InfoLogger()
            elif level == LogLevel.DEBUG:
                LoggerFactory._loggers[LogLevel.DEBUG] = DebugLogger()
            elif level == LogLevel.WARNING:
                LoggerFactory._loggers[LogLevel.WARNING] = WarningLogger()
            elif level == LogLevel.ERROR:
                LoggerFactory._loggers[LogLevel.ERROR] = ErrorLogger()
            else:
                raise ValueError(f"Invalid log level: {level}")
        return LoggerFactory._loggers[level]

# Usage
logger = LoggerFactory.get_logger(LogLevel.INFO)
logger.log("This is an info message.")




"""
# Singleton Logger factory 

class LoggerFactory:
    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerFactory, cls).__new__(cls)
        return cls._instance

    def get_logger(self, level: LogLevel) -> Logger:
        if level not in self._loggers:
            if level == LogLevel.TRACE:
                self._loggers[LogLevel.TRACE] = TraceLogger()
            elif level == LogLevel.INFO:
                self._loggers[LogLevel.INFO] = InfoLogger()
            elif level == LogLevel.DEBUG:
                self._loggers[LogLevel.DEBUG] = DebugLogger()
            elif level == LogLevel.WARNING:
                self._loggers[LogLevel.WARNING] = WarningLogger()
            elif level == LogLevel.ERROR:
                self._loggers[LogLevel.ERROR] = ErrorLogger()
            else:
                raise ValueError(f"Invalid log level: {level}")
        return self._loggers[level]

# Usage
logger_factory = LoggerFactory()
logger = logger_factory.get_logger(LogLevel.INFO)
logger.log("This is an info message.")


"""