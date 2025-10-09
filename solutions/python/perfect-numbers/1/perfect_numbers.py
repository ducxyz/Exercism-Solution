def uoc(number1) :
    liste = []
    for i in range (1, number1) :
        if number1 % i == 0 :
            liste.append(i)
    return liste

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 : 
        raise ValueError("Classification is only possible for positive integers.")
    liste_number = uoc(number)
    somme = 0
    for i in (liste_number) :
        somme += i
    if number == somme :
        return "perfect"
    elif number < somme :
        return "abundant"
    else : 
        return "deficient"
        
