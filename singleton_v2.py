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

print(a,b)

