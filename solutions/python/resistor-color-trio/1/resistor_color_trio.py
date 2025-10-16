list_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def label(colors):
    premier_color = list_colors.index(colors[0])
    deuxieme_color = list_colors.index(colors[1])
    troisieme_color = list_colors.index(colors[2])
    total_ohm = (premier_color * 10 + deuxieme_color ) * 10**(troisieme_color)
    total_change = 0
    if total_ohm >= 1000000000 : 
        total_change = total_ohm // 1000000000
        return str(total_change) + " gigaohms"
    
    if total_ohm >= 1000000 : 
        total_change = total_ohm // 1000000
        return str(total_change) + " megaohms"
    
    if total_ohm >= 1000 :
        total_change = total_ohm // 1000
        return str(total_change) + " kiloohms"
        
    return str(total_ohm) + " ohms"

    
        
        
    
