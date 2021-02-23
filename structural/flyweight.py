from uuid import uuid4
from abc import ABC, abstractmethod

class Flyweight(ABC):
     def __init__(self):
         self._state = str(uuid4())

     @property
     def state(self):
         return self._state

     @abstractmethod
     def operation(self):
         ...


class ConcreteFlyweight(Flyweight):
    def operation(self):
        print("do operation")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        if self._flyweights.get(key):
            flyweight = self._flyweights[key]
        else:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


ff = FlyweightFactory()
objects = []
objects.append(ff.get_flyweight('a'))
objects.append(ff.get_flyweight('b'))
objects.append(ff.get_flyweight('a'))
objects.append(ff.get_flyweight('c'))

for o in objects:
    print(o.state)
