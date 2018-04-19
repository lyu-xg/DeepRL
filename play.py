from agent import Agent
import sys

m, _ = sys.argv[1].split('.')
game, model = m.split('_')

agent = Agent(model)
agent.load_network(sys.argv[1])
while 1:
	agent.simulate()
