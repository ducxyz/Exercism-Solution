import string
alphabet_upper = string.ascii_lowercase.upper()
alphabet_lower = string.ascii_lowercase
number = "0123456789"
def decode(string):
    result = ""
    count = ""
    # Use loop FOR to verifie all element in string
    for i in string : 
        # Check if i is number => keep the number as value count
        if i in number :
            count += i
        elif i in alphabet_upper or i == " " :
            # If no, check count is null or not 
            # If no : combine => change count to int to take the value => repeter i(letter or espace) with number
            if count != "" :
                result += i * int(count)
                count = ""
            # If yes : return the letter to result
            else : 
                result += i 
        # Also but for lower
        elif i in alphabet_lower or i == " " :
            if count != "" :
                result += i * int(count)
                count = ""
            else : 
                result += i 
    return result
                
        


def encode(string):
    result = ""
    count = 1
    if string == "" :
        return result 
    for i in range(1,len(string)) : 
        if string[i] == string[i-1] :
            count += 1
        else : 
            if count > 1 :
                result += str(count) + string[i -1]
            else : 
                result += string[i-1]
            count = 1

    if count > 1 : 
        result += str(count) + string[len(string) -1]
    else : 
        result += string[-1]

    return result
