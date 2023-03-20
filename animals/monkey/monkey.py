from animals import Animal
class Monkey(Animal):
    def __init__(self, name, age, amountOfBananasEaten, hopDistance):
        super().__init__(name, age)
        self.amountOfBananasEaten = amountOfBananasEaten
        self.hopDistance = hopDistance
        
