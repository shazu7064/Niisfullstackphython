 class A:
	def f1(self):
		print("prangya is a person")

 class student(person):
		def f2(self):
			print("prangya is a student")

 class EnginneringStudent(student):
		def f3(self):
			print("prangya is a engineeringStudent")
  ob=EngineeringStudent()
  ob.f1
  ob.f2
  ob.f3 