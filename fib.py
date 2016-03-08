#!/usr/bin/env python3
# Rosalind FIB - eaml
# Rabbits and Recurrence Relations

def litters(months, litter):
	rabbits = 1
	reproductive = 0
	born = 1
	for month in range(months - 1):
		born_last_month = born
		born = reproductive * litter
		reproductive += born_last_month
		rabbits += born
		#print("Month %s: %s born, %s rabbits" % (month, born, rabbits))
	return rabbits

if __name__ == "__main__":
	dataset = input("> ")
	months, litter = map(int, dataset.split())
	print(litters(months, litter))