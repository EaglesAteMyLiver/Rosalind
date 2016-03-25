#!/usr/bin/env python3
# Rosalind SSEQ - eaml
import sys

def subsequence(s, t):
    i_s, i_t = 0, 0
    indexes = []
    while i_s < len(s) and i_t < len(t):
        if t[i_t] == s[i_s]:
            indexes.append(i_s + 1)
            i_t += 1
        i_s += 1
    return indexes

def parse_fasta(data):
    strings = []
    label, last = "", -1
    for line in data.splitlines():
        if line.startswith(">"):
            label = line[1:]
            last += 1
            strings.append([label, ""])
        else:
            strings[last][1] += line
    return strings

if __name__ == "__main__":
    dataset = open(sys.argv[1]).read()
    dataset = parse_fasta(dataset)
    s, t = dataset[0][1], dataset[1][1]
    print(" ".join(map(str, subsequence(s, t))))