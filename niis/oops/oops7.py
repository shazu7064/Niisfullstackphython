#parent Class
class person:
	def __init__(self, name, age):
	    self.name = name    #property
	    self.age =age

	def show_person(self):   #method
		print("Name :",self.name)
		print("Age :",self.age)


#child Class
class student(person):
	def __init__(self, name, age, roll):
	    super().__init__(name,age)   #calling person construct