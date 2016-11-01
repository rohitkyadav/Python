class Student:
	def __init__(self, perc):
		self.percentage = perc
		print("hello")


	def get_per(self):
		
		if self.percentage > 50:
			self.status = True
		
		else:
			self.status = False
		
		return self.percentage

obj = Student(40)
print(obj.get_per())