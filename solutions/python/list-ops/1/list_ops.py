def append(list1, list2):
    # Add all items in list2 to the end of list1
    for i in (list2) : 
        list1.append(i)
    return list1


def concat(lists):
    # Combine 2 liste
    result = []
    for i in lists :
        for j in i : 
            result.append(j) 
    return result
    


def filter(function, list):
    # Return list of all items return true in function
    result = []
    for i in list : 
        if function(i) == True :
            result.append(i)
    return result


def length(list):
    sum = 0 
    for i in list :
        sum += 1
    return sum


def map(function, list):
    # return the list of the rults of applying function(item) on alls items in list
    # Exemple : map(addition x : x+x, [1,2,3]) => [2,4,6]
    result = []
    new = 0
    for i in list : 
        new = function(i)
        result.append(new)
    return result
        


def foldl(function, list, initial):
    acc = initial
    for i in list:
        acc = function(acc, i)
    return acc


def foldr(function, list, initial):
    acc = initial
    for i in reversed(list):
        acc = function(acc, i)
    return acc
    


def reverse(list):
    new_list = []
    for i in range(len(list) - 1, -1, -1) : 
        new_list.append(list[i])
    return new_list
