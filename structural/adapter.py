class Adaptee:
    def __init__(self):
        self._name = ''

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name


class Adapter:
    def __init__(self):
        self._adaptee = Adaptee()

    def get_name(self) -> str:
        return self._adaptee.getName()

    def set_name(self, name: str) -> None:
        self._adaptee.setName(name)


a = Adapter()
a.set_name('n1')
print(a.get_name())
