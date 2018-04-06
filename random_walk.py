from random import choice
class RandomWalk():
	#生成所需的随机数据
	def __init__(self, num_points=5000):
		
		self.num_points = num_points
		#初始为0
		self.x_values = [0]
		self.y_values = [0]
		
	def fill_walk(self):
		#计算所有随机的点
		while len(self.x_values) < self.num_points:
			#方向  距离
			x_direction = choice([1,-10])
			x_distence = choice([0, 1, 2, 3, 4])
			x_step = x_direction * x_distence
			
			y_direction = choice([1,-10])
			y_distence = choice([0, 1, 2, 3, 4])
			y_step = y_direction * y_distence
			
			if x_step == 0 and y_step == 0:
				continue
				
			#计算下一个
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
