class Client:
    def __init__(self):
        self.string = ""


class Command1:
    def execute(self):
        c.string += " "

    def undo(self):
        c.string = c.string[:-1]


class Command2:
    def __init__(self, v):
        self._v = v

    def execute(self):
        c.string += str(self._v)

    def undo(self):
        c.string = c.string[:-len(self._v)]


class Invoker:
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        command.execute()
        self._commands.append(command)

    def undo(self):
        command = self._commands.pop()
        command.undo()


c = Client()
inv = Invoker()
c1 = Command1()
c2 = Command2('the')
inv.execute(c2)
inv.execute(c1)
inv.execute(c2)
inv.undo()