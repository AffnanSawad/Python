class Bird:
    def sound(self):
        print("Bird makes sound")

class Parrot(Bird):
    def sound(self):    # overriding
        print("Parrot says: Hello")

class Crow(Bird):
    def sound(self):    # overriding
        print("Crow says: Caw Caw")

b = Bird()
p = Parrot()
c = Crow()

for x in [b, p, c]:
    x.sound()


# OUTPUT :
# Bird makes sound
# Parrot says: Hello
# Crow says: Caw Caw
