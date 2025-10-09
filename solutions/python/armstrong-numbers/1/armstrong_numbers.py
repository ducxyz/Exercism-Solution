def is_armstrong_number(number):
    str_number = str(number)
    liste = [];
    somme = 0;
    for i in str_number:
        liste.append(i)
    length = len(liste)
    for i in liste :
        somme += int(i)**length
    if somme == number :
        return True
    else:
        return False
        
    
        
    
    
    
    
    
