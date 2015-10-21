###########################################
#          Genetic Algorithim to_         #
#Maximize printable brainfuck ascii output#
#              using evolution            #
#                By Intangere             #
###########################################
from genetics import Genetics, Individual
from operator import add
from brainfuck import Brainfuck, symbols
from random import choice
import string

class Genetics_(Genetics): #We have to subclass Genetics and extend it
	def fitness(self, individual): #Override our fitness function
		if hasattr(individual, 'fitness'):
			pass
		else:
			individual.fitness = 0
		brainfuck = Brainfuck()
		self.idxs = {i : x for i, x in enumerate(symbols)}
		code = ''.join([self.idxs[c] for c in individual.chromosomes])
		try:
			brainfuck.evaluate(code)
			res = brainfuck.output
			nums = []
			for v in list(res):
				nums.append(ord(v))
			for n in nums:
				if chr(n) in string.printable:
					individual.fitness += 1
				else:
					individual.fitness -= 2
			if individual.fitness >= 20:
				self.log("STRONG", individual)
				self.log("OUTPUT of %s" % id(individual), res)
		except Exception as e:
			print "e"
		return individual.fitness

#Goal is to generate brainfuck with maximum ascii values
length = 40
bf = Brainfuck()
abcs = {x : i for i, x in enumerate(symbols)}
idxs = {i : x for i, x in enumerate(symbols)}
World = Genetics_(None) #Define a world where the goal is not defined : ^)
World.population(40, length, 0, idxs.keys()[-1]) #40 individuals, chromosomes match length of target, min = 0, max = highest possible value
for i in xrange(4000): #Loop 4000 times
	World.evolve() #Evolve the population