class Animal:
	def __init__(self, name, age):
		self.name=name
		self.age=age

	def sleep(self):
		print self.name+" of"+self.age+" years old is sleeping!"
	def eat(self):
		print self.name+" of"+self.age+" years old is eating!"
class Bird(Animal):
	def __init__(self, wingcolour, name, age):
		Animal.__init__(self,name, age)
		self.wingcolour=wingcolour
	def fly(self):
		print self.name+" is flying!"

class Dog(Animal):
	def __init__(self, furcolour, name, age):
		Animal.__init__(self, name, age)
		self.furcolour=furcolour
	def bark(self):
		print self.name+" is barking!"

a= Animal("Jack", "23")
a.sleep()
a.eat()