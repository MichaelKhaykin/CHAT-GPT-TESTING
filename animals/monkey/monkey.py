from animals import Animal
class Monkey(Animal):
    def __init__(self, name, age, amountOfBanannasEaten, hopDistance):
        super().__init__(name, age)
        self.amountOfBanannasEaten = amountOfBanannasEaten
        self.hopDistance = hopDistance
