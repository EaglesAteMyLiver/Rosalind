#!/usr/bin/env python3
#Rosalind LCSM - eaml
import sys

def parse_fasta(data):
	strings = {}
	last = ""
	for line in data.splitlines():
		if line.startswith(">"):
			last = line[1:]
			strings[last] = ""
		else:
			strings[last] += line
	return strings

def all_substrings(string):
    result = set()
    for i in range(len(string)):
        for j in range(len(string)-i+1):
            result.add(string[i:i+j])
    return result

def longest_common_substring(data):
    substrings = all_substrings(min(data, key=len))
    common_substrings = [string for string in substrings
        if all(string in x for x in data)]
    return max(common_substrings, key=len)

if __name__ == "__main__":
	dataset = open(sys.argv[1]).read()
	strings = list(parse_fasta(dataset).values())
	print(longest_common_substring(strings))