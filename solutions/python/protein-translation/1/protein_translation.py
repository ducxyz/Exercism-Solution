def proteins(strand):
    liste_proteins = []
    for i in range(0, len(strand), 3) :
        if strand[i:i+3] == "AUG" : 
            liste_proteins.append("Methionine")
        elif strand[i:i+3] in ["UUU", "UUC"] : 
            liste_proteins.append("Phenylalanine")
        elif strand[i:i+3] in ["UUA", "UUG"] : 
            liste_proteins.append("Leucine")
        elif strand[i:i+3] in ["UCU", "UCC", "UCA", "UCG"] : 
            liste_proteins.append("Serine")
        elif strand[i:i+3] in ["UAU", "UAC"] : 
            liste_proteins.append("Tyrosine")
        elif strand[i:i+3] in ["UGU", "UGC"] : 
            liste_proteins.append("Cysteine")
        elif strand[i:i+3] in ["UGG"] : 
            liste_proteins.append("Tryptophan")
        elif strand[i:i+3] in ["UAA", "UAG", "UGA"] : 
            break

    return liste_proteins
        
        
