class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"
