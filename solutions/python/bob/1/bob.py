def response(hey_bob):
    answer = ''
    if hey_bob.strip().endswith('?') :
        answer = 'Sure.'
    if hey_bob.isupper() :
        answer = 'Whoa, chill out!'
    if hey_bob.endswith('?') and hey_bob.isupper() :
        answer = "Calm down, I know what I'm doing!"
    if hey_bob.strip() == '' :
        answer = 'Fine. Be that way!'
    
    if answer == '' :
        answer = 'Whatever.'
    

    return answer
    
                        
    
