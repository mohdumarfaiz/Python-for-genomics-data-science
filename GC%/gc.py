#take input from user
dna = input("Enter a DNA sequence: ").lower()
count = dna.count("g") + dna.count("c")
# Checks whether every character in the DNA sequence is A, T, G, or C.
check = all(base in 'atgc' for base in dna)
#calculate the GC%
if check and len(dna) > 0:
    gc_percentage = count*100/len(dna)
    print("No of G:" , dna.count("g"))
    print("No of C:" , dna.count("c"))
    print(f"GC Percentage: {gc_percentage:.2f}%")
elif 'n' in dna:
    print("DNA sequence contains undefined bases")
else:
    print("The Provided DNA sequence is incorrect (or) No DNA sequence is provided")
