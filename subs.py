#!/usr/bin/env python
# Rosalind SUBS - eaml

def substrings(dna, substring):
	positions = []
	cursor = 0
	while cursor < len(dna):
		found = dna.find(substring, cursor)
		if found == -1:
			break
		cursor = found + 1
		positions.append(cursor)
	return positions

if __name__ == "__main__":
	dna = input("> ")
	substring = input("> ")
	print(" ".join(map(str, substrings(dna, substring))))