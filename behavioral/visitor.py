from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def accept(self, visitor):
        ...


class ComponentA(Component):
    name = "A"
    def accept(self, visitor):
        visitor.visit_a(self)


class ComponentB(Component):
    name = "B"
    def accept(self, visitor):
        visitor.visit_b(self)


class Visitor(ABC):
    @abstractmethod
    def visit_a(selof, cls):
        ...

    @abstractmethod
    def visit_b(selof, cls):
        ...


class Visitor1(Visitor):
    visitor_name = "1"
    def visit_a(self, cls):
        print(f"{self.visitor_name} -> {cls.name}")

    def visit_b(self, cls):
        print(f"{self.visitor_name} -> {cls.name}")


class Visitor2(Visitor):
    visitor_name = "2"
    def visit_a(self, cls):
        print(f"{self.visitor_name} -> {cls.name}")

    def visit_b(self, cls):
        print(f"without log {cls.name}")


components = [ComponentA(), ComponentA(), ComponentB(), ComponentA()]
v1 = Visitor1()
v2 = Visitor2()

for component in components:
    component.accept(v1)
    component.accept(v2)
