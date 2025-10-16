list_vowels = ["a", "e", "i", "o", "u"]
list_rule_1 = ["xr", "yt"]
def handle_rule(text) :
    new_text = ""
    # Check if the first word is begin with vowels or frist two words begin with "xr","yt","ay"
    # Exemple : 
    # "apple" : beginning with a => add "ay" in the end of word => "appleay"
    # "xray" : beginning with xr => add "ay" in the end of word => "xrayay"
    # "yttria" : beginning with yt => add "ay" in the end of word => "yttriaay"
    if text[0] in list_vowels or text[:2] in list_rule_1 :
        new_text = text + "ay"
        return new_text
    consonants = ""
    # Loop for to find consonants until volwels
    for i in text : 
        # Exemple : 
        # "chair" => consonants = "ch" (because after is "a")
        if i not in list_vowels :
            consonants += i
        else : 
            break 
    # If consonants existe
    if consonants :
        # Check if the word start with "qu" => take the word after "u" and add "quay"
        # Rule 3
        if text.startswith("qu") :
            # Exemple : quick
            # Begin with qu => "ick" + "quay" became "ickquay"
            new_text = text[2:] + "quay"
            return new_text
        # If not in the condition up => in the Rule 2
        else : 
            # Exemple : chair
            # text[len(consonants):] = air + "ch" + "ay" => "airchay"
            new_text = text[len(consonants):] + consonants + "ay"
    # Rule 3 : have consonants + qu || "square" || consonants : sq
    # Check if consonants endwith q and the third word is u
    if consonants.endswith("q") and text[len(consonants)] == "u" :
        # Exemple : "square"
        # consonnant = sq => new_text = "are" + "sq" + "uay" => aresquay
        new_text = text[len(consonants) + 1:] + consonants + "uay"
        return new_text

    # RULE 4 : rhythm
    consonants_before_y = ""
    # consonants = rhythm
    for i in consonants :
        # for i = "r" => consonants_before_y = "r"
        # for i = "h" => consonants_before_y = "rh"
        # for i = "y" => finish the bool
        if i != "y" :
            # consonants_before_y = rh
            consonants_before_y += i
        # Finish the bool after meet "y"
        else :
            break
    # If consonants_before_y existe
    if consonants_before_y :
        # new_text = "yth" + "rh" + "ay"
        new_text = text[len(consonants_before_y):] + consonants_before_y + "ay"

    return new_text

def translate(text):
    # Split to the liste
    text_liste = text.split()
    length = len(text_liste)
    res = ""
    n = 1
    # Loop for all the condition in the handle_rule(text)
    for text in text_liste : 
        new_text = handle_rule(text)
        if n < length :
            # Add a space between words (except for the last one)
            new_text += " "
            n += 1
        res += new_text
    return res

        

    
        
        
        
    
    
            
        
        
