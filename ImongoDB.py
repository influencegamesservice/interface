from pymongo import MongoClient
from abc import ABCMeta, abstractmethod
import mainsetting

class Abstractmongodb(metaclass=ABCMeta):

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