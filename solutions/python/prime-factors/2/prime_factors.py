def factors(value):
    if value <= 1 : 
        return []
    liste_prime = []
    div = 2
    while value > 1 :
        if value % div == 0 :
            liste_prime.append(div)
            value = value // div
        else :
            div += 1

    return liste_prime
            