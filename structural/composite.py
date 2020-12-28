from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_name(self):
        ...


class Leaf(Component):
    def get_name(self):
        print(self._name)


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def get_name(self):
        for component in self._components:
            component.get_name()

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)


l1 = Leaf('l1')
l2 = Leaf('l2')
l3 = Leaf('l3')
box2 = Composite('B2')
box2.add_component(l3)
box1 = Composite('B1')
box1.add_component(l1)
box1.add_component(l2)
box1.add_component(box2)
box1.get_name()
