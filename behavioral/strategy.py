from abc import ABCMeta, abstractmethod

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute(self):
        self._strategy().func()

class Strategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def func(self):
        pass


class StrategyA(Strategy):
    def func(self):
        print 'strategyA'


class StrategyB(Strategy):
    def func(self):
        print 'strategyB'


context = Context(StrategyA)
context.execute()
