import math


class MagicClass:
	def __init__(self, radius=0):
		self.__radius = radius

	@property
	def radius(self):
		return self.__radius

	@radius.setter
	def radius(self, value):
		if not isinstance(value, int) and not isinstance(value, float):
			raise TypeError("radius must be a number")
		self.__radius = value

	def area(self):
		return math.pi * self.__radius ** 2

	def circumference(self):
		return math.pi * 2 * self.__radius
