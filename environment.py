import random
DEFX=10
DEFY=10
class Environment:
	def __init__(self,xsize=DEFX,ysize=DEFY):
		self.things={}
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
		for category in self.things:
			for thing in self.things[category]:
				thing.step()
#		for agent in self.things['agent']:
#			agent.step()
		self.show()
	def look(self,x,y):
		xt=x+1
		yt=y+1
		surroundings=[]
		for row in self.grid[yt-1:yt+2]:
			tmp=row[xt-1:xt+2]
			surroundings.append(tmp)
		return surroundings
	def transpose(self,x,y):
		assert(x>=0 and x<self.xsize)
		assert(y>=0 and y<self.ysize)
		xt=x+1
		yt=y+1
		return (xt,yt)
	def occupied(self,x,y):
		(xt,yt)=self.transpose(x,y)
		if self.grid[yt][xt]=='.':
			return False
		return True
	def randomAvailable(self):
		x=random.randint(0,self.xsize-1)
		y=random.randint(0,self.ysize-1)
		x0=x
		y0=y
		while True:
			x=x+1
			if x>=self.xsize:
				x=0
				y+=1
				if y>=self.ysize:
					y=0
			if not self.occupied(x,y):
				return (x,y)
			if x==x0 and y==y0:
				return None
	def insert(self,item,x,y):
		itemName=item.name
		assert(itemName!=None)
		if itemName in self.things:
			self.things[itemName].append(item)
		else:
			self.things[itemName]=[item]
		symbol=item.symbol
		(xt,yt)=self.transpose(x,y)
		assert(self.grid[yt][xt]=='.')
		self.grid[yt][xt]=symbol
