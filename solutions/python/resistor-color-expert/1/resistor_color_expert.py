list_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
tolerance_colors = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
tolerance_values  = ["±0.05%", "±0.1%", "±0.25%", "±0.5%", "±1%", "±2%", "±5%", "±10%"]

def resistor_label(colors) :
    if len(colors) == 1 :
        return '0 ohms'
    elif len(colors) == 4 :
        return resistor_label_four(colors)
    elif len(colors) == 5 :
        return resistor_label_five(colors)
    


def resistor_label_four(colors):
    premier_color = list_colors.index(colors[0])
    deuxieme_color = list_colors.index(colors[1])
    troisieme_color = list_colors.index(colors[2])
    index_quatrieme_color = tolerance_colors.index(colors[3])
    tolerance = tolerance_values[index_quatrieme_color]
    
    total_ohm = (premier_color * 10 + deuxieme_color ) * 10**(troisieme_color)

    total_change = 0
    if total_ohm >= 1000000 : 
        total_change = total_ohm / 1000000
        ohms = str(total_change) + " megaohms"
    
    elif total_ohm >= 1000 :
        total_change = total_ohm / 1000
        if total_change.is_integer():
            total_change = int(total_change)
        ohms = str(total_change) + " kiloohms"
    else :     
        ohms = str(total_ohm) + " ohms"
    
    return ohms + " " + str(tolerance)


def resistor_label_five(colors):
    premier_color = list_colors.index(colors[0])
    deuxieme_color = list_colors.index(colors[1])
    troisieme_color = list_colors.index(colors[2])
    quatrieme_color = list_colors.index(colors[3])
    index_cinquieme_color = tolerance_colors.index(colors[4])
    tolerance = tolerance_values[index_cinquieme_color]
    
    total_ohm = (premier_color * 100 + deuxieme_color * 10 + troisieme_color ) * 10**(quatrieme_color)

    total_change = 0
    if total_ohm >= 1000000 : 
        total_change = total_ohm / 1000000
        ohms = str(total_change) + " megaohms"
    
    elif total_ohm >= 1000 :
        total_change = total_ohm / 1000
        if total_change.is_integer():
            total_change = int(total_change)
        ohms = str(total_change) + " kiloohms"
    else : 
        ohms = str(total_ohm) + " ohms"
    
    return ohms + " " + str(tolerance)

    
    
    
