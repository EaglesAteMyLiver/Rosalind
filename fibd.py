#!/usr/bin/env python3
# Rosalind FIBD - eaml
# Mortal Fibonacci Rabbits

def mortal(months, live):
	time_to_live = [0 for i in range(live-1)] + [1]
	for month in range(months-1):
		# Each pair of breeding age (older than one month) will
		#  reproduce, creating a new pair.
		born = sum(time_to_live[:-1])
		# Ages the population by one month, by shifting it to the
		#  left (thus killing off all rabbits older than live 
		#  months)
		time_to_live = time_to_live[1:]
		# Adds the newborns to the general population.
		time_to_live.append(born)
	return sum(time_to_live)

if __name__ == "__main__":
	dataset = input("> ")
	months, live = map(int, dataset.split())
	print(mortal(months, live))