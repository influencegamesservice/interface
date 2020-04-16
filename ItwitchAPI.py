from abc import ABCMeta, abstractmethod
from requests import Response
import mainsetting

class ABtwitchAPI(metaclass=ABCMeta):

    @abstractmethod
    def get_top_games(self, first=None, after=None, before=None) -> Response:
        pass

    @abstractmethod
    def get_game_streams(self, after=None, before=None, first=None, game_id=None, language=None, user_id=None, user_login=None) -> Response:
        pass

class ABtwitchANA(metaclass=ABCMeta):
    @staticmethod
    def get_bucket_remaining(response):
        return response.headers['ratelimit-remaining']

    @staticmethod
    def shape_top_games(response):
        return response.json()['data']
    
    @staticmethod
    def get_top_games_pagination(response):
        return response.json()['pagination']
    
    @staticmethod
    def shape_game_stream(response):
        return response.json()['data']
    
    @staticmethod
    def get_game_stream_pagination(response):
        return response.json()['pagination']
    
    @staticmethod
    def get_game_info_from_json(json):
        info = {"viewer":0, "streamer":0}
        for elem in json:
            info["viewer"] += int(elem['viewer_count'])
            info["streamer"] += 1
        return info
    
    @staticmethod
    def processing_game_info(json, game_info):
        for elem in mainsetting.twsetting.MUST_GET_GAME_INFO_FORM_JSON:
            game_info[elem] = json[elem]
        return game_info
    
    @staticmethod
    def get_status_code(response):
        return response.status_code