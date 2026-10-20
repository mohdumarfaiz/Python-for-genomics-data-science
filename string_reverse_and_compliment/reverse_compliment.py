def main():
    dna = input("DNA Sequence: ").lower()
    print(rc(dna))

def rc(dna):
    r = dna[::-1]
    bank = {'a' : 't', 'g' : 'c', 'c' : 'g', 't' : 'a'}
    characters = list(r)
    characters = [bank[base] for base in characters]
    return ''.join(characters)

main()