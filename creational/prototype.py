from abc import ABC, abstractmethod
from copy import copy, deepcopy

class Prototype(ABC):
    def __init__(self, type, value):
        self._type = type
        self._value = value

    @abstractmethod
    def clone(self):
        ...

    def __str__(self):
        return f"Type: {self._type}, value: {id(self._value)};"


class ConcretePrototypeA(Prototype):
    def __init__(self, type, value):
        self._type = type
        self._value = value

    def clone(self):
        return self.__class__(f"copy_{self._type}", copy(self._value))


class ConcretePrototypeB(Prototype):
    def __init__(self, type, value):
        self._type = type
        self._value = value

    def clone(self):
        return self.__class__(f"copy_{self._type}", deepcopy(self._value))


value = [1, 2, 3]
cpa = ConcretePrototypeA('concrete_prototype_a', value)
cpb = ConcretePrototypeA('concrete_prototype_b', value)
copy_1 = cpa.clone()
copy_2 = cpa.clone()
print(copy_1, copy_2)
copy_3 = cpb.clone()
print(copy_3)