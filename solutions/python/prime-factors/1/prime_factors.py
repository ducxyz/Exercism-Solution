def factors(value):
    if value <= 1 : 
        return []
    liste_prime = []
    div = 2
    while value > 1 :
        while value % div == 0 :
            liste_prime.append(div)
            value = value // div
        div += 1

    return liste_prime
            