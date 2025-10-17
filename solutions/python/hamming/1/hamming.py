def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b) :
        raise ValueError("Strands must be of equal length.")
    count = 0
    # Use loop for :
    # Exemple : a : "ATG" b : "AAA" for len("ATG") = 3 => i = 0, 1, 2
    # i = 0 => "A" == "A" => continue
    # i = 1 => "T" != "A" => different => count = 1
    # i = 2 => "G" != "A" => different => count = 2
    for i in range (len(strand_a)) : 
        if strand_a[i] == strand_b[i] : 
            continue 
        else : 
            count += 1

    return count 
