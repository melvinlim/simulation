NAME='agent'
class Agent:
	def __init__(self,env=0,x=0,y=0,symbol='a'):
		assert(env!=0)
		self.env=env
		self.x=x
		self.y=y
		self.name=NAME
		self.symbol=symbol
	def look(self):
		return self.env.look(self.x,self.y)
	def step(self):
		surroundings=self.look()
		print surroundings
