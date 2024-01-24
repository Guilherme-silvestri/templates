import abc

class LogProviderInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def debug(self, log: str):
        raise NotImplementedError

    @abc.abstractmethod
    def info(self, log: str):
        raise NotImplementedError

    @abc.abstractmethod
    def critical(self, log: str):
        raise NotImplementedError