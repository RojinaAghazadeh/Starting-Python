class circle():
	pi = 3.145926
	def __init__(self,r):
		self.r = r
	def area(self):
		a = self.r * self.r * self.pi
		return a
c1 = circle(10)
print(c1.area())
