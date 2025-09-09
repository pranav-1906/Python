class Herbivore:
    def grass(self):
        print("This animal is a herbivore")

class Carnivore:
    def meat(self):
        print("This animal is carnivore")


class Cow(Herbivore):
    pass

class Tiger(Carnivore):
    pass

#class inherits 2 other classes
class Crow(Herbivore, Carnivore):
    pass

cow = Cow()
tiger = Tiger()
crow = Crow()

cow.grass()
tiger.meat()
crow.grass()
crow.meat()