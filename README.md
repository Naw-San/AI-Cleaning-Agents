# AI-Cleaning-Agents

Three different AI Cleaning Agents called RandomizedAgent, ReflexAgent, and ModelBasedAgent.

#RandomizedAgent
It is a simple AI-based cleaning agent to navigate and clean on given environment with random movement.
The goal of this agent is as simple as description, the agent randomly moves around the environment and 
the suck() function sucks the dirt randomly.

#ReflexAgent
This agent is slightly better than RandomizedAgent, for immediate decision based on environment.
The agent moves randomly, but the suck() function only suck/clean dirt, when the agent detects it.

#ModelBasedAgent
Unlike previous agents, ModelBasedAgent builds and maps internal "map" of environment. It remembers where
it has been and state of those locations (clean or dirty). This knowledge allows it to make better priortize decisions
such as moving to unvisited locations.
