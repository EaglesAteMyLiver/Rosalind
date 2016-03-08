#!/usr/bin/env python3
# Rosalind #1 - eaml

def count_nucleotides(string):
	count = {"A": 0, "C": 0, "G": 0, "T": 0}
	for nucleotide in string:
		count[nucleotide] += 1
	return count["A"], count["C"], count["G"], count["T"]

if __name__ == "__main__":
	dataset = input("> ")
	print("%s %s %s %s" % count_nucleotides(dataset))