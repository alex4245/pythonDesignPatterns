from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @property
    def imp(self):
        return self._imp

    @imp.setter
    def imp(self, i):
        self._imp = i

    @abstractmethod
    def do_operation(self):
        ...


class Product1(AbstractProduct):
    def do_operation(self):
        print(f"product1 {self.imp.operation()}")


class Product2(AbstractProduct):
    def do_operation(self):
        print(f"product2 {self.imp.operation()}")


class ImpA:
    def operation(self):
        return "impA"

class ImpB:
    def operation(self):
        return "impB"


p1 = Product1()
p1.imp = ImpB()
p1.do_operation()
