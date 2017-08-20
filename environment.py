DEFX=10
DEFY=10
class Environment:
	def __init__(self,xsize=DEFX,ysize=DEFY):
		self.xsize=xsize
		self.ysize=ysize
		self.grid=[[' ']*xsize]*ysize
		for i in self.grid:
			print i
	def step(self):
		pass
