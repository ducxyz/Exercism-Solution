def is_isogram(string):
    
    word = ""
    for i in string.lower() :
        if i not in word or i == '-' or i == " " :
            word = word + i
        
    if len(word) < len(string) :
        return False
    return True
    
