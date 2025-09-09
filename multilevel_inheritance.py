#grandparent class
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

#parent classes
class Herbivore(Animal):
    def grass(self):
        print(f"{self.name} is a herbivore")

class Carnivore(Animal):
    def meat(self):
        print(f"{self.name} is carnivore")

#child classes
class Cow(Herbivore):
    pass

class Tiger(Carnivore):
    pass

class Crow(Herbivore, Carnivore):
    pass

cow = Cow("maadu")
tiger = Tiger("puli")
crow = Crow("Kaaka")

cow.eat()
tiger.eat()
crow.eat()

cow.grass()
tiger.meat()
crow.grass()
crow.meat()