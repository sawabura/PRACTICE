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
    pass

class Secretary(Worker):
    pass


