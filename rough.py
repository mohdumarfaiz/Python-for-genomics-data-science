dna=input("Enter DNA sequence:")

dna_counts={'t':dna.count('t'),'c':dna.count('c'),'g':dna.count('g'),'a':dna.count('a')}

nt=sorted(dna_counts.keys())

print(nt[-1])