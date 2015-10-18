###########################################
#          Genetic Algorithim lib         #
#                 By Phc                  #
###########################################
from genetics import Genetics, Individual
from operator import add

class Genetics_(Genetics): #We have to subclass Genetics and extend it

	def fitness(self, individual): #Override our fitness function
		individual.fitness = 0
		for x, y in zip(individual.chromosomes, target):
			if x == y:
				individual.fitness += 1
		return abs(len(self.target) - individual.fitness)

	def fittest(self): #Get a individual whose chromosomes are the solution
		for individual in self.population:
			if individual.fitness == len(target):
				return individual

target_text = "Hello folks!!".lower()
symbols = list("abcdefghijklmnopqrstuvwxyz !@#$%^&*()_+[];':\",./<>?1234567890~`")
abcs = {x : i for i, x in enumerate(symbols)}
idxs = {i : x for i, x in enumerate(symbols)}
target = [abcs[x] for x in target_text]
World = Genetics_(target) #Define a world where the goal is to have numbers = 100
World.population(40, len(target), 0, idxs.keys()[-1]) #40 individuals, chromosomes match length of target, min = 0, max = target value
fitness_history = [World.grade()]
for i in xrange(200000): #Loop 200000 times
	World.evolve() #Evolve the population
	fitness_history.append(World.grade()) #Store the populations grade
	res = ''.join([idxs[x] for x in World.population[0].chromosomes])
	World.log("INFO, iter %s" % i, res)
	if target_text == res:
		World.log("SOLVED", World.fittest())
		break
