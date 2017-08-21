NAME='thing'
SYMBOL='-'
class Thing(object):
	def __init__(self,env=0,x=0,y=0):
		assert(env!=0)
		self.env=env
		self.x=x
		self.y=y
		#self.name=NAME
		#self.symbol=SYMBOL
	def step(self):
		pass
