from abc import ABCMeta, abstractmethod


class Observable:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass


class Channel(Observable):
    def add_message(self, message):
        self.notify_observers(message)


class User(Observer):
    def __init__ (self, username):
        self._username = username

    def update(self, message):
        print '%s: %s' % (self._username, message)


channel = Channel()
u1 = User('user_1')
u2 = User('user_2')
channel.add_observer(u1)
channel.add_observer(u2)
channel.add_message('test')
