from models.base import Base

class Rectangle(Base):
	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		if type(value) != int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		if type(value) != int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value

	def area(self):
		return self.__width * self.__height

	def display(self):
		for i in range(self.__x):
			print()
		for j in range(self.__height):
			print(" " * self.__y + "#" * self.__width)

	def update(self, *args, **kwargs):
		attributes = ['id', 'width', 'height', 'x', 'y']
		if args and args is not None:
			for i, value in enumerate(args):
				if i < len(attributes):
					setattr(self, attributes[i], value)
		elif kwargs:
			for k, v in kwargs.items():
				if k in attributes:
					setattr(self, k, v)

	def to_dictionary(self):
		return {
			"id": self.id,
			"width": self.width,
			"height": self.height,
			"x": self.x,
			"y": self.y
		}

	def __str__(self):
		return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,self.id, self.__x, self.__y, self.__width, self.__height )