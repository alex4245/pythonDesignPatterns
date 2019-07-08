class A(object):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

a = A()
b = A()

print (a, b)
