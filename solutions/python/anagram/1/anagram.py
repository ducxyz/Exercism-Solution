def find_anagrams(word, candidates):
    word = word.lower()
    signature_word = sorted(word)

    result = []

    for i in candidates : 
        signature_i = i
        i = i.lower()
        if i == word : 
            continue
        i = sorted(i)
        if signature_word == i : 
            result.append(signature_i)

    return result
