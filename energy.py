from thing import Thing
NAME='energy'
SYMBOL='*'
class Energy(Thing):
	def __init__(self,env=0,x=0,y=0):
		super(Energy,self).__init__(env,x,y)
		self.name=NAME
		self.symbol=SYMBOL
	def step(self):
		pass
