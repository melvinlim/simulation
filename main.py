from environment import Environment
from agent import Agent
from energy import Energy
SIMTIME=1000
def insertEnergy(env,x,y):
	energy=Energy(env,x,y)
	env.insert(energy,x,y)
def insertAgent(env,x,y):
	agent=Agent(env,x,y)
	env.insert(agent,x,y)
def init(env):
	insertAgent(env,0,0)
	insertAgent(env,0,5)
	insertAgent(env,1,2)
	insertAgent(env,3,3)
	for i in range(4):
		(x,y)=env.randomAvailable()
		insertEnergy(env,x,y)
enviro=Environment()
init(enviro)
for t in range(SIMTIME):
	enviro.step()
