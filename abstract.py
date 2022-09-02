from dataclasses import dataclass


class FakeClass:
    def print_fake(self):
        print("THE WORLD IS A FAKE!")


class MetaTest(type):
    def __new__(cls, class_name, bases, attrs: dict):
        attrs.update({"maxil": 1, "sss": 34})
        return type.__new__(cls, class_name, bases, attrs)
    # def __init__(cls, class_name, bases, attrs: dict):
    #     type.__init__(cls, class_name, bases, attrs)
    #     print(cls)
    #     print(class_name)
    #     print(bases)
    #     print(attrs)
    #     cls.MAX = None



@dataclass
class Dog(FakeClass, metaclass=MetaTest):

    age: int | float = 1
    breed: str = "unknown"

d = Dog()
d.print_fake()
print(Dog.__dict__)








class Animals(type):
    def create_attrs(self, *args):
        for k, v in self.standart_attrs.items():
            self.__dict__[k] = v


    def __init__(cls, name, bases, attrs):
        cls.standart_attrs = attrs | {"name_class": name, "bases": bases}
        cls.__init__ = Animals.create_attrs




@dataclass
class Cat(metaclass=Animals):
    breed: str = "standart"
    age: int = "1"



cat1 = Cat()
print(cat1.__dict__)


@dataclass
class Antylope(metaclass=Animals):
    color: str
    size: float
    age: int
    horns_sized: float

print(Antylope.standart_attrs)
ant1 = Antylope("red", 25, 21, 3)














