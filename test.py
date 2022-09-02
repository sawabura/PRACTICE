from abc import abstractmethod, ABCMeta
import shelve
from dataclasses import dataclass


class Test(metaclass=ABCMeta):
    @abstractmethod
    def sit(self):
        pass

    @abstractmethod
    def stand(self):
        pass


class Player(Test):
    def sit(self):
        pass


names = ['Оля', 'Вася', 'Коля']
surnames = ['Петрова', 'Пупкин', 'Смирнов']

with shelve.open("conservation") as shelf:
    shelf["names"] = names
    shelf["surnames"] = surnames
    shelf.sync()

from typing import NamedTuple


class Tuple_from_typing(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Tuple_from_typing:
    return Tuple_from_typing(10, 20)


w = get_gps_coordinates()
print(w)

from collections import namedtuple

tup = namedtuple("tup_without_class", ["latitude", "logitude"])
print(tup(2, 2))
print(tup.__dict__)


class Tuple_From_Collections(namedtuple("Tuple_From_Collections", ["latitude", "logitude"])):
    __slots__ = ()


print(Tuple_From_Collections(1, 2))


