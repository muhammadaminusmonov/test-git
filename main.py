class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"I am {self.name} {self.surname} and i am {self.age} old"
greeting()

def is_equal(a, b):
    return a == b
