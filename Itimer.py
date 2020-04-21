from abc import ABCMeta, abstractmethod

class ABtimer(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass