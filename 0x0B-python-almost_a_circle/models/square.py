from models.rectangle import Rectangle


class Square(Rectangle):
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)

	@property
	def size(self):
		return self.width

	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		attributes = ['id', 'size', 'x', 'y']
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
			"size": self.size,
			"x": self.x,
			"y": self.y
		}

	def __str__(self):
		return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,self.id, self.x, self.y, self.width)