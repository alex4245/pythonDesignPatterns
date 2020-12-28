from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def method1(self):
        ...

    @abstractmethod
    def method2(self):
        ...

    def template_method(self):
        self.method1()
        self.method2()


class ConcreteSubjectA(Subject):
    def method1(self):
        print(f"Method 1, subject A")

    def method2(self):
        print(f"Method 2, subject A")


class ConcreteSubjectB(Subject):
    def method1(self):
        print(f"Method 1, subject B")

    def method2(self):
        print(f"Method 2, subject B")


a = ConcreteSubjectA()
b = ConcreteSubjectB()
a.template_method()
b.template_method()