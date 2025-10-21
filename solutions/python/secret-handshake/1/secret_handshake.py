def commands(binary_str):
    liste_action = []
    liste_number = list(binary_str)
    liste_number.reverse()
    bit = ""
    for i in range(len(liste_number)):
        bit = liste_number[i]
        if bit == "1" :
            if i == 0 : 
                liste_action.append("wink")
            elif i == 1 : 
                liste_action.append("double blink")
            elif i == 2 : 
                liste_action.append("close your eyes")
            elif i == 3 : 
                liste_action.append("jump")
            elif i == 4 : 
                liste_action.reverse()

        elif bit == 0 :
            continue

    return liste_action
            
            
        
        
