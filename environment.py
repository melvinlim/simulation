DEFX=10
DEFY=10
class Environment:
	def __init__(self,xsize=DEFX,ysize=DEFY):
		self.objects={}
		self.xsize=xsize
		self.ysize=ysize
		self.grid=[]
		for i in range(ysize):
			self.grid.append(['.']*xsize)
#		self.grid=[['.']*xsize]*ysize
		self.show()
#		for i in self.grid:
#			print i
	def show(self):
		for row in self.grid:
			for cell in row:
				print cell,
			print
		print
	def step(self):
		self.show()
	def insert(self,item,itemName,x,y):
		if itemName in self.objects:
			self.objects[itemName].append(item)
		else:
			self.objects[itemName]=[item]
		symbol=item.symbol
		assert(x<self.xsize)
		assert(y<self.ysize)
		assert(self.grid[x][y]=='.')
		self.grid[x][y]=symbol
