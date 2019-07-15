from abc import ABCMeta, abstractmethod

class Handler:
    __metaclass__ = ABCMeta
    
    _successor = None
    def set_successor(self, successor):
        self._successor = successor
        return successor

    def call_successor(self):
        if self._successor:
            self._successor.handle()

    @abstractmethod
    def handle(self):
        pass


class HandlerA(Handler):
    def handle(self):
        print 'handleA'
        self.call_successor()


class HandlerB(Handler):
    def handle(self):
        print 'handleB'
        self.call_successor()


class HandlerC(Handler):
    def handle(self):
        print 'handleC'
        self.call_successor()


hA = HandlerA()
hB = HandlerB()
hC = HandlerC()

hA.set_successor(hB).set_successor(hC)
hA.handle()
