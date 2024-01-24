from logbook import Logger, StreamHandler
import sys
from src.domain.ports.logprovider import LogProviderInterface


class LogProvider(LogProviderInterface):
    def __init__(self) -> None: 
        StreamHandler(sys.stdout).push_application()
        log = Logger('Logbook')
        self.debug = log.debug
        self.info = log.info
        self.critical = log.critical

    def debug(log: str):
        pass

    def info(log: str):
        pass

    def critical(log: str):
        pass