#!/usr/bin/env python3
# Rosalind TRAN - eaml
import sys

def is_transition(a, b):
    return a+b in ["AG", "GA", "CT", "TC"]

def is_transversion(a, b):
    return a+b in ["AC", "CA", "AT", "TA", "GC", "CG", "GT", "TG"]

def transitions(s1, s2):
    return sum(map(is_transition, s1, s2))

def transversions(s1, s2):
    return sum(map(is_transversion, s1, s2))

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

if __name__ == "__main__":
    dataset = open(sys.argv[1]).read()
    s1, s2 = list(parse_fasta(dataset).values())
    print(transitions(s1, s2) / transversions(s1, s2))