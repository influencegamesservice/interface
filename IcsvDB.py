from abc import ABCMeta, abstractmethod

class ABStwitchCsvDataBase(metaclass=ABCMeta):
    """twitch用のCSSDataBaseの抽象クラス"""

    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        """start関数は常に依存関係が無く、いつでもどこでも呼べる"""
        pass

    @abstractmethod
    def check_twitch_game_data_is_new(self, game_data) -> bool:
        pass

    @abstractmethod
    def insert_twitch_game_data(self, game_data):
        pass

    @abstractmethod
    def update_twitch_game_data(self, game_data):
        pass