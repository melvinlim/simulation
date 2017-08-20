from environment import Environment
SIMTIME=1000
enviro=Environment()
for t in range(SIMTIME):
	enviro.step()
