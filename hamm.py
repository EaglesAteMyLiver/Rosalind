#!/usr/bin/env python3
# Rosalind HAMM - eaml

def hamming_distance(s_1, s_2):
	return sum(map(lambda a, b: a!=b, s_1, s_2))

if __name__ == "__main__":
	string_1 = input("> ")
	string_2 = input("> ")
	print(hamming_distance(string_1, string_2))