"""
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""

def DNA_strand(dna):
	output = []
	for i in dna:
		if i == 'A':
			output.append('T')
		elif i == 'T':
			output.append('A')
		elif i == 'G':
			output.append('C')
		else:
			output.append('G')
	return ''.join(output)

def DNA_strand_v2(dna):
	return dna.translate(str.maketrans('ATCG','TAGC'))