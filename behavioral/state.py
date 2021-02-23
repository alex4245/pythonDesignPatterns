from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class StateA(State):
    def operation1(self):
        print("operation 1A")

    def operation2(self):
        print("operation 2A")


class StateB(State):
    def operation1(self):
        print("operation 1B")

    def operation2(self):
        print("operation 2B")


class Context:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        self._state = state

    def do_operation1(self):
        self._state.operation1()

    def do_operation2(self):
        self._state.operation2()


sa = StateA()
sb = StateB()
c = Context()
c._state = sa
c.do_operation1()
c.do_operation2()
c._state = sb
c.do_operation1()
c.do_operation2()