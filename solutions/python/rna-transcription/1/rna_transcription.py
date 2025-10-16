def to_rna(dna_strand):
    rna = ""
    for i in dna_strand : 
        if i == "G" :
            i = "C"
            rna += i
        elif i == "C" :
            i = "G"
            rna += i
        elif i == "T" :
            i = "A"
            rna += i
        elif i == "A" :
            i = "U"
            rna += i

    return rna
