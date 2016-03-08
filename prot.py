#!/usr/bin/env python3
# Rosalind PROT - eaml

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

if __name__ == "__main__":
	dataset = "".join(open(input("> ")).read().splitlines())
	print(rna_to_protein(dataset))