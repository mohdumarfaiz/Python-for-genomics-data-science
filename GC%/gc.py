dna = input("Enter a DNA sequence: ").lower()
count = dna.count("g") + dna.count("c")
check = all(base in 'atgc' for base in dna)
if check and len(dna) > 0:
    gc_percentage = count*100/len(dna)
    print("No of G:" , dna.count("g"))
    print("No of C:" , dna.count("c"))
    print(f"GC Percentage: {gc_percentage:.2f}%")
else:
    print("The Provided DNA sequence is incorrect (or) No DNA sequence is provided")
