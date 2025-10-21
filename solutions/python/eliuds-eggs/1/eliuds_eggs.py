def egg_count(display_value):
    liste_binary = []
    while display_value > 0 :
        if display_value % 2 == 1 :
            liste_binary.append(1)
            display_value //= 2
        elif display_value % 2 == 0 :
            liste_binary.append(0)
            display_value //= 2
    liste_binary.reverse()
    sum_of_egg = 0
    for i in liste_binary : 
        if i == 1 :
            sum_of_egg += 1
        elif i == 0 :
            continue

    return sum_of_egg
            
