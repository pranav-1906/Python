class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} squeaks!")


dog1 = Dog("Subramani")
cat1 = Cat("Keo")
mouse1 = Mouse("Mickey")

print(dog1.name)
print(cat1.name)
print(mouse1.name,"\n")

dog1.eat()
cat1.eat()
mouse1.eat()
dog1.sleep()
cat1.sleep()
mouse1.sleep()
dog1.speak()
cat1.speak()
mouse1.speak()