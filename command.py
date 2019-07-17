from abc import ABCMeta, abstractmethod
import datetime


class Reciver:
    def get_date(self):
        return datetime.date.today()

    def get_date_time(self):
        return datetime.datetime.now()


class Button:
    __metaclass__ = ABCMeta

    def __init__(self, reciver):
        self._reciver = reciver
        
    @abstractmethod
    def push(self):
        pass
    

class PasteDateButton(Button):
    def push(self):
        return self._reciver.get_date()


class PasteDatetimeButton(Button):
    def push(self):
        return self._reciver.get_date_time()

class Invoker:
    def __init__(self, cmd):
        self._cmd = cmd

    def execute(self):
        print self._cmd.push()


reciver = Reciver()
dt_button = PasteDatetimeButton(reciver)
invoker = Invoker(dt_button)
invoker.execute()
