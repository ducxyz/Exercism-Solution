def reverse(text):
    # Create new text
    new_text = ""
    # Using loop exemple : racecar 
    # Loop 1 : i = r => new_text = "r" + "" => new_text = "r"
    # Loop 2 : i = a => new_text = "r" + "a" => new_text = "ra"
    # Loop 3 : i = c => new_text = "ra" + "c" => new_text = "rac"
    # Loop 4 : i = e => new_text = "rac" + "e" => new_text = "race"
    # Loop 5 : i = c => new_text = "race" + "c" => new_text = "racec"
    # Loop 6 : i = a => new_text = "racec" + "a" => new_text = "raceca"
    # Loop 7 : i = r => new_text = "raceca" + "r" => new_text = "racecar"
    for i in (text) :
        new_text = i + new_text
    # Return new words
    return new_text
