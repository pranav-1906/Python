class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_info(self):
        print(f"{self.name} is a {self.species}")

    def can_eat(species):
        valid_species = ['hen','goat','fish','cow']
        return species in valid_species
    
animal1 = Animal('shishimaru','dog')
animal2 = Animal('chikku','hen')

print(Animal.can_eat('dog'))
print(Animal.can_eat('hen'))
print(animal1.get_info())
print(animal2.get_info())