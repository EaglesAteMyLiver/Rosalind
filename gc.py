#!/usr/bin/env python3
# Rosalind GC - eaml

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

def gc_content(string):
	return (string.count("C") + string.count("G")) / len(string) * 100

if __name__ == "__main__":
	data = ""
	line = input()
	while line:
		data += line + "\n"
		line = input()

	strings = parse_fasta(data)
	print("%s\n%s" % max(((label, gc_content(data)) 
		for label, data in strings.items()), key=lambda i: i[1]))