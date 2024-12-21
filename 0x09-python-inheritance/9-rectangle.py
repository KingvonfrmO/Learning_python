BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height

	def area(self):
		return self.__height * self.__width

	def __str__(self):
		string = "[" + str(__class__.__name__) + "] "
		string += str(self.__width) + "/" +str(self.__height)
		return string