CODON_TO_PROTEIN = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyrosine",  
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",  
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
    "UAA" : "STOP",
    "UAG" : "STOP",
    "UGA" : "STOP",
}

def proteins(strand):
    result = []

    for i in range(0, len(strand), 3):
        protein = CODON_TO_PROTEIN.get(strand[i : i + 3])
        if protein == "STOP":
            break
        result.append(protein)
    
    return result


print(proteins("UGGUAG"))