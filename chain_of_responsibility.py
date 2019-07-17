from abc import ABCMeta, abstractmethod

class Handler:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def handle(self):
        pass


class HandlerA(Handler):
    def handle(self):
        print 'handleA'


class HandlerB(Handler):
    def handle(self):
        print 'handleB'


class Client:
    def __init__(self):
        self._lst_handlers = []

    def add_handler(self, handler):
        self._lst_handlers.append(handler)

    def start_handle(self):
        for h in self._lst_handlers:
            h.handle()


ha = HandlerA()
hb = HandlerB()
c = Client()
c.add_handler(ha)
c.add_handler(hb)
c.start_handle()
