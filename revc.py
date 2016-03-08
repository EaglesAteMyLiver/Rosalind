#!/usr/bin/env python3
# Rosalind #3 - eaml

def complement(string):
	complements = {"A":"T", "T":"A", "C":"G", "G":"C"}
	return "".join(complements[symbol] for symbol in string)

def reverse_complement(string):
	return complement(string[::-1])

if __name__ == "__main__":
	dataset = input("> ")
	print(reverse_complement(dataset))