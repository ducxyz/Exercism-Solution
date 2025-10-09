import string
def is_valid(isbn):
    # get string of alphabet uppercase
    alphabet_upper_case = string.ascii_uppercase 
    # replace hyphens to empty blank
    number_isbn = isbn.replace("-", "")
    # check if isbn after replace hyphens with length 10 or not null
    if len(number_isbn) != 10 or not number_isbn : 
        return False
    value = 10
    total = 0
    index = 0
    # loop each string number in the string number isbn 
    for i in number_isbn :
        # Check if number isbn contains X and X is the last position
        if i == 'X' and index == 9 :
            i = 10
        # If not => check if number isbn in the list of alphabet(include X)
        elif i in alphabet_upper_case :
            return False
        # Calculer total of the number isbn : 
        # - Change from string to int because i is caractere in string number isbn 
        # - Value - index because value initial = 10 (10-digits isbn) and index = 0 (start from index 0 of string) 
        # - Exemple : 3-598-21508-8 => 3598215088 => 3 : value 10 index : 0 => 3 * (10 - 0) => 5 * (value 10 - index 1) => ...
        total += int(i) * (value - index )
        index += 1
    # Check if total is modulo of 11 or no
    if total % 11 == 0:
        return True
    return False
        
    
