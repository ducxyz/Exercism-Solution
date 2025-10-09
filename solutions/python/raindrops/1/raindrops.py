def convert(number):
    text = ''
    if number % 3 == 0 :
        text += 'Pling'
    if number % 5 == 0 :
        text += 'Plang'
    if number % 7 == 0 :
        text += 'Plong'

    if number % 7 == 0 and number % 5 == 0 and number % 3 == 0 :
        text = 'PlingPlangPlong'

    if number % 7 != 0 and number % 5 != 0 and number % 3 != 0 :
        return str(number)

    return text
