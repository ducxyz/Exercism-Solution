def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.replace('_', ' ')
    liste = words.split()
    new_words = ""
    for i in range(len(liste)) : 
        for j in range(len(liste[i])) :
            if j == 0 :
                new_words += liste[i][j].upper()

    return new_words
                
