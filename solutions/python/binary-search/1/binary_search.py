def find(search_list, value):
    if value not in search_list : 
        raise ValueError("value not in array")
    left = 0
    right = len(search_list) - 1
    while left <= right :
        mid = (right + left) // 2
        if search_list[mid] == value :
            return mid
        elif search_list[mid] < value :
            left = mid + 1
        else :
            right = mid - 1
            

        
    
    