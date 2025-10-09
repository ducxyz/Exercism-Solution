import string
def is_pangram(sentence):
    number = "0123456789"
    if not sentence :
        return False
    alphabet = string.ascii_lowercase
    sentence_no_blank = sentence.replace(" ","")
    caractere = '[@_!#$%^&*()<>?/\|}{~:]".'
    word = ""
    for i in sentence_no_blank :
        if i.lower() not in word and i.lower() not in caractere and i not in number :
            word = word + i
        
    if len(alphabet) == len(word) :
        return True
    return False
