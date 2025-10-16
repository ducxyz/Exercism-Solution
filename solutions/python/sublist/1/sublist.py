"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "none"
    
def sublist(list_one, list_two):
    # Check if all the element of list 1 is the same list 2 => EQUAL (also with 2 list null)
    if list_one == list_two:
        return EQUAL
    # Check list 2 is contained in 1 → list 2 is a superlist
    elif is_sublist(list_one, list_two):
        return SUPERLIST
    # Check list 1 is contained in list 2 → list 1 is a sublist
    elif is_sublist(list_two, list_one):
        return SUBLIST
    return UNEQUAL


def is_sublist(one, two):
    # Loop for to see if list 2 appear in list 1 or not 
    # Exemple : list 1 = [1,2,3,4] ; list 2 = [2,3]
    # + len(list1) = 4, len(list2) = 2 => i in range(3) => i = 0, 1, 2
    # + use *len(one) - len(two) + 1* because its show how many couple we verifie list 2 in          list 1
    # + we verifie in couple [1,2] [2,3] [3,4] : 3 time with 3 i = 0, i = 1, i = 2
    for i in range(len(one) - len(two) + 1):
        # Check if list 2 is empty => is sublist
        # Or list 2 = list one[i : i + len(list_2)]
        # Exemple : 
        # + list 2 = [2,3], list 1 = [1,2,3,4]
        # + we verifie : 
        # + for i = 0 => one[0:2] = [1,2] => not in
        # + for i = 1 => one[1,3] = [2,3] => in => return TRUE
        # + for i = 2 => one[2,4] = [3,4] => not in
        if not two or two == one[i : i + len(two)]:
            return True
    return False
    
    
    
    
    
