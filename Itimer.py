from abc import ABCMeta, abstractmethod
import mainsetting

class ABtimer(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass