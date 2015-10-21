###########################################
#           Genetic Algorithim to         #
#   Find values that add up to a number   #
#              By Intangere               #
###########################################
from genetics import Genetics, Individual

World = Genetics(100) #Define a world where the goal is to have numbers = 100
World.population(30, 6, 0, World.target) #10 individuals, 5, chromosomes each, min = 0, max = target value
fitness_history = [World.grade()] #Only needed to view fitness history
solutions = []
for x in xrange(200): #Loop 100 times
	World.evolve() #Evole the population
	fitness_history.append(World.grade()) #Store the populations grade
	if World.grade() == 0.0:
		solutions.append(World.population[0].chromosomes)
World.log("FITNESS HISTORY", str(fitness_history)) #Print our fitness results after loops completed
World.log("SOLUTIONS", str(solutions))
