class Singleton:
    instance = None
    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()

def singleton(cls):
    _instance = {}
    def get():
        if not _instance.get(cls):
            _instance[cls] = cls()
        return _instance[cls]
    return get

@singleton
class A: pass

a = A()
b = A()




