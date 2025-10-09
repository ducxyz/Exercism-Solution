def rotate(text : str, key : int): 
    # Get the string of alphabet caractere
    plain_lower = "abcdefghijklmnopqrstuvwxyz"
    plain_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_caractere = "0123456789'[@_!#$%^&*()<>?/\|}{~:].,"
    
    # Initialise a cipher text to return
    cipher = ""
    # Loop each caractere in text original 
    for i in text :
        # Get the position of caractere in the plain
        if i != " " and i not in number_caractere :
            if i.islower() :
                index = plain_lower.index(i)
                plain = plain_lower
            else :
                index = plain_upper.index(i)
                plain = plain_upper
            # Calculer the cipher to return 
            # Exemple : omg with ROT5 
            # Loop 1 : i = 'o' => index of 'o' is 15 in the plain => + key = 5 => caractere position 20 in plain => cipher = 't'
            # Loop 2 : i = 'm' => index of 'm' is 13 in the plain => + key = 5 => caractere position 18 in plain => cipher = 'tr'
            # Loop 3 : i = 'g' => index of 'g' is 7 in the plain => + key = 5 => caractere position 12 in plain => ciphet = 'trl'
            idx_cipher = index + key
            if idx_cipher >= 26 :
                idx_cipher = idx_cipher - 26
            cipher += plain[idx_cipher]
        elif i in number_caractere :
            cipher += i
        else : 
            cipher += " "
    return cipher