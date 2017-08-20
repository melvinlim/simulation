from environment import Environment
from agent import Agent
SIMTIME=1000
def insertAgent(env,x,y):
	agent=Agent(x,y)
	env.insert(agent,agent.name,x,y)
def init(env):
	insertAgent(env,1,2)
	insertAgent(env,3,3)
enviro=Environment()
init(enviro)
for t in range(SIMTIME):
	enviro.step()
