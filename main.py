from dataclasses import dataclass, field


@dataclass
class Worker():
    __extra_attributes = {
        "insurance": True,
        "wages_bonus_percent": 20,
    }

    @classmethod
    def create_worker(cls, name, salary):
        return cls(name, salary)

    name: str
    salary: int

    # def __post_init__(self):
    #     self.__dict__ = Worker.__extra_attributes


class Manager(Worker):

    def grow_salary(self):
        pass


class Secretary(Worker):
    pass


w1 = Worker.create_worker("VVV", 30000)

m1 = Manager.create_worker("VVsadasV", 30000)
