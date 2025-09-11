
# OOP: simple class and object

class PersonalInfo:

    def __init__( self , name , age , salary):
        self.name = name 
        self.age = age
        self.salary = salary

    def showInfo(self):
        print(f"My name is {self.name} , {self.age} years old and my Salary is ${self.salary}")


student1 = PersonalInfo("Affnan Sawad", 30, 120000) 

student1.showInfo()


# Class + Object
class Cars:

    def __init__(self,name,model):

        self.name = name
        self.model = model

    def show(self):
        print(f"I have a {self.name} car and model is {self.model}")    


car1 = Cars("Toyota" , "Prado")
car2 = Cars("Honda", "CRV")

car1.show()
car2.show()