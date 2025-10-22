def flatten(iterable):
    result = []
    for i in iterable :
        # isinstance for checking the condition
        # exemple : isinstance(5, int) => true 
        if isinstance(i, list) : 
            # result.extend : to combine 2 list 
            # exemple : result = [1,2,3] , result_2 = [4,5,6]
            # result.extend(result_2) = [1,2,3,4,5,6]
            #
            # use recursion to take the whole list
            # Exemple : iterable = [1,[2,[3,4]],5]
            # Take the list [2,[3,4]] 
            # flatten([2,[3,4]] => relauche again the fonction => 2 is not the list => result = 2
            # [3, 4] is a list => result.extend(flatten([3,4])) => relauche the fonction again
            # 3 and 4 not is a list => result = 2, 3 ,4
            result.extend(flatten(i))
        elif i is not None :
            result.append(i)
    return result

