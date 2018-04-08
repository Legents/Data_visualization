from random import randint

class Die():
	#模拟骰子的类
	def __init__(self, num_sides=6):
		#默认为六面的骰子
		self.num_sides = num_sides
		
	def roll(self):
		return randint(1, self.num_sides)
