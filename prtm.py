#!/usr/bin/env python3
#Rosalind PRTM - eaml

monoisotopic_mass = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333"""

Monoisotopic_mass = {amminoacid: float(mass) 
	for amminoacid, mass 
	in map(str.split, monoisotopic_mass.splitlines())
}

def protein_weight(protein):
	return sum(map(lambda a: Monoisotopic_mass[a], protein))

if __name__ == "__main__":
	dataset = input("> ")
	print(protein_weight(dataset))