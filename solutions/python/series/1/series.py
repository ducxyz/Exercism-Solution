def slices(series, length):
    if length == 0 :
        raise ValueError("slice length cannot be zero")
    elif length < 0 : 
        raise ValueError("slice length cannot be negative")

    if series == "" : 
        raise ValueError("series cannot be empty")

    if length > len(series) : 
        raise ValueError("slice length cannot be greater than series length")
    liste_new = []
    for i in range(len(series) - length + 1) : 
        liste_new.append(series[i:i+length])

    return liste_new
        
        
        
    
