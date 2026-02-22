import string
def rows(letter):
    alphabet = string.ascii_lowercase.upper()
    alphabet = list(alphabet)
    position = 0
    letters = []
     # Use loop FOR to find the position of letter
    for i in range(len(alphabet)) :
        # Add the letter in the list letters
        letters.append(alphabet[i])
        # If the letter append in the list egalite with letter the user input => stop to find the next one
        # Exemple : use input : "B"
        # First loop : letters = ['A'] , A is not the letter user enter
        # Second loop : letters = ['A', 'B'] , alphabet[i] = 'B' egalite user input = 'B' => stop 
        if alphabet[i] == letter.upper() :
            position = i + 1 
            break
    diamon = []
    line = ""
    outer = 0 
    inner = 0
    # Use loop FOR to print the hafl upper diamon
    for i in range(position) :
        # For i = 0 => caractere = 'A' 
        # For i = 1 => caractere = 'B'
        caractere = letters[i]
        # outer = position - i - 1 because : 
        # letters = ['A', 'B'] => the line with 'A' have " A " => 1 outer
        #                         the line with 'B' have "B B" => 0 outer
        # The space its 1 when down line + outer minus 1 when i inc => position - 1 - i
        outer = position - i - 1
        # Write the first line with letter 'A'
        if i == 0 :
            line = " " * outer + caractere + outer * " "
        # Write the suivants letter
        else : 
            # inner = 2 * i -1 because : 
            # letters = ['A', 'B', 'C'] => the line with 'A' have " A " => 0 outer
            #                              the line with 'B' have "B B" => 1 inner
            #                              the line with 'C' have"C   C" => 3 inner
            # The space its +2 each line => arithmetic progression with the space = 2
            # aₙ = a₁ + (n - 1) * d => with 'B' => a1 : i = 1, d = 2 => aₙ = 1 + (i - 1) * 2 = 2 * i - 1
            inner = 2 * i - 1
            line = " " * outer + caractere + " " * inner + caractere + " " * outer

        diamon.append(line)
    # Print le half down of diamond => if position = 3 with letter = 'C' => i in range(1, -1, -1)
    # Explain (1, -1, -1) => i = 0 , 1 => its mean from 1 to -1 (stop 0) with space -1
    # Take from the list the element before 'C' and print in the last list
    for i in range(position - 2, -1, -1) :
        diamon.append(diamon[i])

    return diamon
        
        
        
        
            
            
        
