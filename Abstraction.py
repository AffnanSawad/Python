

class Vehicle():          # Abstract class
   
    def start(self):
        pass

  
    def stop(self):
        pass


class Car(Vehicle):          # must implement abstract methods
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

car = Car()
car.start()
car.stop()

# ✅ Abstraction → only necessary details, hide complexity.