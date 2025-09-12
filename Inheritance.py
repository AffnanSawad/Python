# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class (inherits Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        # call parent constructor
        super().__init__(name, age)
        self.student_id = student_id

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")


# create objects
p1 = Person("Affnan", 21)
s1 = Student("Sawad", 20, "CSE-101")

p1.show()  # from parent
s1.show()  # from child



# Multiple
class Father:
    def skill(self):
        print("Programming")

class Mother:
    def hobby(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()  # Programming
c.hobby()  # Cooking



# Multilevel
class Grandfather:
    def house(self):
        print("Has a big house")

class Father(Grandfather):
    def car(self):
        print("Has a car")

class Son(Father):
    def bike(self):
        print("Has a bike")

s = Son()
s.house()  # from Grandfather
s.car()    # from Father
s.bike()   # from Son

# Hierrachiel
class Animal:
    def move(self):
        print("Animals can move")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.move(); d.bark()
c.move(); c.meow()
