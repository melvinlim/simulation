from thing import Thing
NAME='agent'
SYMBOL='a'
class Agent(Thing):
	def __init__(self,env=0,x=0,y=0):
		super(Agent,self).__init__(env,x,y)
#		assert(env!=0)
#		self.env=env
#		self.x=x
#		self.y=y
		self.name=NAME
		self.symbol=SYMBOL
	def disp(self,surroundings):
		for row in surroundings:
			for col in row:
				print col,
			print
	def look(self):
		surroundings=self.env.look(self.x,self.y)
		self.disp(surroundings)
		return surroundings
	def step(self):
		surroundings=self.look()
