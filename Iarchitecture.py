from abc import ABCMeta, abstractmethod

class ABSFlaskServerModel(metaclass=ABCMeta):
    pass

class ABmodel(metaclass=ABCMeta):

    @abstractmethod
    def get_now_games_info(self) -> tuple:
        pass

    @abstractmethod
    def processing_all_game_info(self, all_game_info:dict) -> dict:
        pass

    @abstractmethod
    def processing_all_streamer_info(self, all_streamer_info:dict) -> dict:
        pass

    @abstractmethod
    def set_all_game_info_to_MongoDB(self, all_game_info:dict):
        pass

    @abstractmethod
    def set_all_streamer_info_to_MongoDB(self, all_streamer_info:dict):
        pass

    @abstractmethod
    def set_all_game_info_to_CSS(self, all_game_info:dict):
        pass

    @abstractmethod
    def set_all_streamer_info_to_CSS(self, all_streamer_info:dict):
        pass

class ABcontroller(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass
