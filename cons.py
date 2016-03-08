#!/usr/bin/env python3
#Rosalind CONS - eaml
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

def profile_matrix(data):
    profile = [[0 for i in range(len(data[0]))] 
        for j in range(4)]
    for string in data:
        for i, nucleotide in enumerate(string):
            profile["ACGT".find(nucleotide)][i] += 1
    return profile

def consensus(profile):
    return "".join("ACGT"[max(range(4), key=lambda j: profile[j][i])] 
        for i in range(len(profile[0])))

if __name__ == "__main__":
    dataset = open(sys.argv[1]).read()
    dataset = list(parse_fasta(dataset).values())
    profile = profile_matrix(dataset)
    consensus_string = consensus(profile)
    print(consensus_string)
    for i in range(4):
        print("ACGT"[i] + ": " + " ".join(map(str, profile[i])))