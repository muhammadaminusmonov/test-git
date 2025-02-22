
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.info = None

    def __str__(self):
        return f"I am {self.name} {self.surname} and i am {self.age} old"

    def bio(self, info):
        self.info = info
