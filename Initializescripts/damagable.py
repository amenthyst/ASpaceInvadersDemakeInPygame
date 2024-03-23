from abc import abstractmethod, ABC
# like a type: this object can be damaged
class damagable(ABC):
    @abstractmethod
    def damage(self, damage):
        pass


