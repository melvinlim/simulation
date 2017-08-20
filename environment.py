DEFX=10
DEFY=10
class Environment:
	def __init__(self,xsize=DEFX,ysize=DEFY):
		self.objects={}
		self.xsize=xsize
		self.ysize=ysize
		self.grid=[]
		self.grid.append([' ']*(xsize+2))
		for i in range(ysize):
			self.grid.append([' ']+['.']*xsize+[' '])
		self.grid.append([' ']*(xsize+2))
		self.show()
	def show(self):
		for row in self.grid:
			for cell in row:
				print cell,
			print
		print
	def step(self):
		for agent in self.objects['agent']:
			agent.step()
		self.show()
	def look(self,x,y):
		xt=x+1
		yt=y+1
		surroundings=[]
		for row in self.grid[yt-1:yt+2]:
			tmp=row[xt-1:xt+2]
			surroundings.append(tmp)
	def insert(self,item,itemName,x,y):
		if itemName in self.objects:
			self.objects[itemName].append(item)
		else:
			self.objects[itemName]=[item]
		symbol=item.symbol
		assert(x>=0 and x<self.xsize)
		assert(y>=0 and y<self.ysize)
		xt=x+1
		yt=y+1
		assert(self.grid[yt][xt]=='.')
		self.grid[yt][xt]=symbol
