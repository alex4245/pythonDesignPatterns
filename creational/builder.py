from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        ...

    @abstractmethod
    def build_part_b(self):
        ...

    @abstractmethod
    def build_part_c(self):
        ...


class ConcreteBuilder1(Builder):
    def build_part_a(self):
        print("Build 1.A")

    def build_part_b(self):
        print("Build 1.B")

    def build_part_c(self):
        print("Build 1.C")


class Director:
    def __init__(self):
        self._builder = None

    def add_builder(self, builder):
        self._builder = builder

    def construct_small(self):
        print("Build small")
        self._builder.build_part_a()

    def construct_large(self):
        print("Build large")
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()


director = Director()
cb1 = ConcreteBuilder1()
director.add_builder(cb1)
director.construct_large()
director.construct_small()