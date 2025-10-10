def rotate(text : str, key : int): 
    # Get the string of alphabet caractere
    plain_lower = "abcdefghijklmnopqrstuvwxyz"
    plain_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_caractere = "0123456789'[@_!#$%^&*()<>?/\|}{~:].,"
    
    # Initialise a cipher text to return
    cipher = ""
    # Loop each caractere in text original 
    for i in text :
        #Check the index of i not is a blank and not is number and caractere
        if i != " " and i not in number_caractere :
            # Check the index, if its lower => take the index in the plain with lower
            if i.islower() :
                # Get the position of caractere in the plain
                index = plain_lower.index(i)
                plain = plain_lower
            # Else take the index in the plain with upper
            else :
                index = plain_upper.index(i)
                plain = plain_upper
            # Take the index after addition the key => take the caractere of cipher
            idx_cipher = index + key
            # Check if the index of cipher is greater than 26 => index cipher - 26 to take the initial position
            if idx_cipher >= 26 :
                idx_cipher = idx_cipher - 26       
            # Calculer the cipher to return 
            # Exemple : omg with ROT5 
            # Loop 1 : i = 'o' => index of 'o' is 15 in the plain => + key = 5 => caractere position 20 in plain => cipher = 't'
            # Loop 2 : i = 'm' => index of 'm' is 13 in the plain => + key = 5 => caractere position 18 in plain => cipher = 'tr'
            # Loop 3 : i = 'g' => index of 'g' is 7 in the plain => + key = 5 => caractere position 12 in plain => ciphet = 'trl'
            cipher += plain[idx_cipher]
        # Check index is number or caractere => take the same number caractere
        elif i in number_caractere :
            cipher += i
        # If have blank => take the blank
        else : 
            cipher += " "
    return cipher