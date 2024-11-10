from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def store(self, entity_obj):
        pass
    
    @abstractmethod
    def find(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, entity_obj):
        pass
    
    @abstractmethod
    def delete(self, entity_id):
        pass
