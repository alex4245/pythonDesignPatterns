from abc import ABC, abstractmethod


class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Channel(Subject):
   ...


class User(Observer):
    def __init__ (self, username):
        self._username = username

    def update(self, message):
        print(f"{self._username}, {message}")


channel = Channel()
u1 = User('user_1')
u2 = User('user_2')
channel.add_observer(u1)
channel.add_observer(u2)
channel.notify_observers('test')
