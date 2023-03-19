from animals import Animal

class Cat(Animal):
    def __init__(self, name, age, meowNoiseLevel):
        super().__init__(name, age)
        self.meowNoiseLevel = meowNoiseLevel