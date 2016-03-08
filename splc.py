#!/usr/bin/env python3
# Rosalind SPLC - eaml
import sys

rna_codon = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

RNA_Codon = {}
for line in map(str.split, rna_codon.splitlines()):
    for n in range(4):
        RNA_Codon[line[n*2]] = line[n*2+1]

def rna_to_protein(rna):
    protein = ""
    for n in range(len(rna) // 3):
        codon = rna[n*3:n*3+3]
        amminoacid = RNA_Codon[codon]
        if amminoacid == "Stop":
            break
        else:
            protein += amminoacid
    return protein

def transcribe(string):
    return string.replace("T", "U")

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

def remove_introns(data, introns):
    while True:
        found = False
        for intron in introns:
            position = data.find(intron)
            if position > 0:
                data = data[:position] + data[position+len(intron):]
                found = True
        if not found:
            return data

if __name__ == "__main__":
    dataset = open(sys.argv[1]).read()
    dataset = parse_fasta(dataset)
    dna_string, introns = dataset[0][1], [string[1] for string in dataset[1:]]
    print(rna_to_protein(transcribe(remove_introns(dna_string, introns))))