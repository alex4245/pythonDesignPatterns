from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, request):
        pass

class HandlerA(Handler):
    def handle(self, request):
        if request == "a":
            print("handle A")
            return True


class HandlerB(Handler):
    def handle(self, request):
        if request == "b":
            print("handle B")
            return True


class Client:
    def __init__(self):
        self._lst_handlers = []

    def add_handler(self, handler):
        self._lst_handlers.append(handler)

    def start_handle(self, request):
        for h in self._lst_handlers:
            if h.handle(request):
                break


ha = HandlerA()
hb = HandlerB()
c = Client()
c.add_handler(ha)
c.add_handler(hb)
c.start_handle(request="b")
