class parent(object):
	"""docstring for inher"""
	def __init__(self, last_name,eye_color):
		print('parent __init__ things')
		self.last_name=last_name
		self.eye_color=eye_color

	def show_info(self):
		print("Last_name " + self.last_name)
		print("Eye_color " + self.eye_color)

class child(parent):
	"""docstring for child"""
	def __init__(self, last_name,eye_color,toys):
		print("child __init__")
		parent.__init__(self,last_name,eye_color)
		self.toys = toys
		
	def show_info(self):
		print("Last_name -" + self.last_name)
		print("Eye_color -" + self.eye_color)
		print("Toys -" + self.toys)

# brad = parent('pit','Red')
# brad.show_info()

emma = child('watson','blue','wand')
emma.show_info()
# print(emma.last_name)
# print(emma.eye_color)
# print(emma.toys)