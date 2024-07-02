from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
