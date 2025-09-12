# 1. Encapsulation

# 👉 Binding data & methods together in one unit (class) and controlling access using private/public.

# Public (self.name) → Accessible everywhere

# Protected (self._salary) → Shouldn’t be accessed outside (but possible)

# Private (self.__bank_balance) → Cannot be accessed directly outside


class Employee:
    def __init__(self, name, salary):
        self.name = name           # public
        self._salary = salary      # protected
        self.__bank_balance = 5000 # private

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}")

    def show_balance(self):   # controlled access
        print(f"Bank Balance: {self.__bank_balance}")


emp = Employee("Affnan", 1200)
emp.show_info()         # OK
emp.show_balance()      # OK
