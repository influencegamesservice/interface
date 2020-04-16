from pymongo import MongoClient
from abc import ABCMeta, abstractmethod

class ABSBaseMongoDB(metaclass=ABCMeta):

    def __init__(self):
        self.DB_of_Twitch = MongoClient()['Twitch']
        self.Collection_of_Common = self.DB_of_Twitch.Common
        self.Collection_of_Games = self.DB_of_Twitch.Games
        self.Collection_of_Streamers = self.DB_of_Twitch.Streamers
    
    @staticmethod
    def ALLDOCUMENTclear(collection):
        collection.delete_many({})
    
    @staticmethod
    def DOCUMENTinsert(collection, docs):
        collection.insert_one(docs)
    
    @staticmethod
    def DOCUMENTupdate_many(collection, filter, update):
        collection.update_many(filter, update)
    
    @staticmethod
    def ALLDOCUMENTprint(collection):
        documents = collection.find({})
        for d in documents:
            print(d)

class Abstractmongodb(ABSBaseMongoDB):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def DBinitialize(self):
        pass

    @abstractmethod
    def set_game_info(self, game_json):
        pass

    @abstractmethod
    def set_streamer_info(self, streamer_json):
        pass