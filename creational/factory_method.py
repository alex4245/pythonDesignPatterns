class ObjectA:
    def function(self):
        print("Object A")


class ObjectB:
    def function(self):
        print("Object B")


def factory_method(object_type):
    objects = {
        "A": ObjectA,
        "B": ObjectB
    }
    o = objects.get(object_type)
    if not o:
        print("Get default object")
        o = ObjectA
    return o

a = factory_method("A")
a().function()
b = factory_method("B")
b().function()
d = factory_method("AAAA")
d().function()
