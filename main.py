from dataclasses import dataclass


@dataclass
class Worker():
    insurance = True

    @classmethod
    def create_worker(cls, name, salary):
        return cls(name, salary)

    name: str
    salary: int


class Manager(Worker):
    __extra_attributes = {}

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__dict__ = Manager.__extra_attributes


class Secretary(Worker):
    pass


m1 = Worker.create_worker("VVV", 30000)

m2 = Manager.create_worker("VVsadasV", 30000)
