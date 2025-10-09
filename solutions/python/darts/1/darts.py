import math
def score(x, y):
    number = 0
    distance = math.sqrt(x**2 + y**2)
    if (-10 <= distance <= 10):
        number = 1 
    if (-5 <= distance <= 5):
        number = 5
    if (-1 <= distance <= 1):
        number = 10

    return number
    
    
