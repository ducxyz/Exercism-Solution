import string 
alphabet = list(string.ascii_lowercase)
cipher = alphabet[::-1]
def encode(plain_text):
    plain_text = list(plain_text.lower())
    new_text = ""
    for i in plain_text :
        if i in alphabet :
            text = alphabet.index(i)
            new_text += cipher[text]
        else : 
            new_text += i
    new_text = list(new_text)
    cleaned = ""
    for i in new_text :
        if i in [" ", ".", ","] :
            continue
        cleaned += i
    groupe_5 = ""
    for i in range(0, len(cleaned), 5) :
        groupe_5 += cleaned[i : i + 5] + " "
    groupe_5 = groupe_5.strip()
    return groupe_5
    
    
def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ","")
    ciphered_text = list(ciphered_text)
    new_liste_text = []
    text_index = 0
    for i in ciphered_text :
        if i in cipher :
            text_index = cipher.index(i)
            new_liste_text += alphabet[text_index]
        else : 
            new_liste_text += i

    new_text = ""
    for i in new_liste_text : 
        new_text += i

    return new_text
        
        
        




    
    
