from animals import Animal
class Dog(Animal):
	def __init__(self, name, age, dogBreed):
		super().__init__(name, age)
		self.breed = dogBreed
