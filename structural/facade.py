class Subsystem1:
    def init(self):
        print("subsystem1: inited")

    def start(self):
        print("subsystem1: started")


class Subsystem2:
    def __init__(self):
        self._parameter = ''

    def on(self) -> None:
        print("subsystem2: started")

    @property
    def parameter(self) -> str:
        return self._parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self._parameter = parameter


class Facade:
    def start(self):
        s1 = Subsystem1()
        s1.init()
        s1.start()
        s2 = Subsystem2()
        s2.parameter = 'p1'
        s2.on()

f = Facade()
f.start()