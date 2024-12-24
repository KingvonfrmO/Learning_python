import json
import csv
import turtle


class Base:
	__nb_objects = 0
	def __init__(self, id = None):
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		if list_dictionaries is None or len(list_dictionaries) == 0:
			return "[]"
		else:
			return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		filename = cls.__name__ + ".json"
		with open(filename, "w") as f:
			if list_objs is None:
				f.write("[]")
			else:
				list_dict = [o.to_dictionary() for o in list_objs]
				f.write(Base.to_json_string(list_dict))

	@staticmethod
	def from_json_string(json_string):
		if json_string is None or len(json_string) == 0:
			return []
		else:
			return json.loads(json_string)

	@classmethod
	def create(cls, **dictionary):
		if dictionary and dictionary != {}:
			if cls.__name__ == "Rectangle":
				new = cls(1, 1)
			else:
				new = cls(1)
			new.update(**dictionary)
			return new
	@classmethod
	def load_from_file(cls):
		filename = cls.__name__ + ".json"
		try:
			with open(filename, "r") as f:
				list_dicts = Base.from_json_string(f.read())
				return [cls.create(**dictionary) for dictionary in list_dicts]
		except IOError:
			return []

	@classmethod
	def save_to_file_csv(cls, list_objs):
		filename = cls.__name__ + ".csv"
		with open(filename, "w", newline="") as f:
			if list_objs is None or list_objs == []:
				csvfile.write("[]")
			else:
				if cls.__name__ == "Rectangle":
					fieldnames = ["id", "width", "height", "x", "y"]
				else:
					fieldnames = ["id", "size", "x", "y"]
				writer = csv.DictWriter(f, fieldnames=fieldnames)
				for obj in list_objs:
					writer.writerow(obj.to_dictionary())

	@classmethod
	def load_from_file_csv(cls):
		filename = cls.__name__ + ".csv"
		try:
			with open(filename, "r", newline="") as f:
				if cls.__name__ == "Rectangle":
					fieldnames = ["id", "width", "height", "x", "y"]
				else:
					fieldnames = ["id", "size", "x", "y"]
				list_dicts = csv.DictReader(f, fieldnames=fieldnames)
				list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
				return [cls.create(**d) for d in list_dicts]
		except IOError:
			return []

	@staticmethod
	def draw(list_rectangles, list_squares):
		screen = turtle.Screen()
		screen.bgcolor("white")
		screen.title("Drawing Shapes")

		drawer = turtle.Turtle()
		drawer.shape("turtle")
		drawer.speed(2)

		# Draw rectangles
		for rect in list_rectangles:
			drawer.penup()
			drawer.goto(rect.x, -rect.y)
			drawer.pendown()
			drawer.fillcolor("blue")
			drawer.begin_fill()
			for _ in range(2):
				drawer.forward(rect.width)
				drawer.left(90)
				drawer.forward(rect.height)
				drawer.left(90)
			drawer.end_fill()

		# Draw squares
		for square in list_squares:
			drawer.penup()
			drawer.goto(square.x, -square.y)
			drawer.pendown()
			drawer.fillcolor("green")
			drawer.begin_fill()
			for _ in range(4):
				drawer.forward(square.size)
				drawer.left(90)
			drawer.end_fill()

		drawer.hideturtle()
		screen.mainloop()