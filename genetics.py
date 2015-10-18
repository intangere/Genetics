###########################################
#           Genetic Algorithim lib        #
#                   By Phc                #
###########################################
from random import random, randint
from operator import add

class Individual(object):
	def __init__(self, chromosomes, min, max):
		self.chromosomes = [randint(min, max) for x in xrange(chromosomes)]
		self.min = min
		self.max = max
	def __repr__(self):
		return "<Individual %s>: Chromosomes -> %s, Min -> %s, Max -> %s " % (id(self), self.chromosomes, self.min, self.max)

class Genetics(object):
	
	def __init__(self, target):
		self.target = target

	def __repr__(self):
		x = ""
		for Individual in self.population:
			x = '\n'.join([x, str(Individual)])
		return x

	def log(self, info, message):
		print "[%s]: %s" % (info, message)

	def population(self, amount, chromosomes, min, max):
		self.population = [Individual(chromosomes, min, max) for x in xrange(amount)]
		self.amount = amount
		
	def fitness(self, individual):
		sum = reduce(add, individual.chromosomes, 0)
		return abs(self.target - sum)

	def grade(self):
		summed = reduce(add, (self.fitness(individual) for individual in self.population), 0)
		return summed / float(len(self.population))

	def mutate(self, parents, chance_to_mutate = 0.1):
		for individual in parents:
			if chance_to_mutate > random():
				chromosome_to_mutate = randint(0, len(individual.chromosomes) - 1)
				individual.chromosomes[chromosome_to_mutate] = randint(individual.min, individual.max)

	def breed(self, parents, parents_length, desired_length):
		children = []
		while len(children) < desired_length:
			male = randint(0, parents_length - 1)
			female = randint(0, parents_length - 1)
			if male != female:
				male, female = parents[male], parents[female]
				half = len(male.chromosomes) / 2
				child = Individual(len(male.chromosomes), male.min, male.max) #Create a new individual 
				child.chromosomes = male.chromosomes[:half] + female.chromosomes[half:] #Mix chromosomes
				children.append(child)
		parents.extend(children)
		return parents

	def evolve(self, retain = 0.2, random_select = .05, mutate = 0.1):
		graded = [ (self.fitness(individual), individual) for individual in self.population ]
		graded = [ individual[1] for individual in sorted(graded) ]
		retain_length = int(len(graded) * retain)
		parents = graded[:retain_length]
		for individual in graded[retain_length:]:
			if random_select > random():
				parents.append(individual)
		parents_length = len(parents)
		desired_length = len(self.population) - parents_length
		self.mutate(parents)
		self.population = self.breed(parents, parents_length, desired_length)


