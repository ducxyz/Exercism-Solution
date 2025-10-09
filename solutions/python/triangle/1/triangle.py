def isvalide(sides):
    a,b,c = sides 
    if (a + b >= c) and (a + c >= b) and (b + c >= a) :
        return True

    return False

def equilateral(sides):
    if not isvalide(sides) :
        return False
    a,b,c = sides
    if (a == 0) or (b==0) or (c==0):
        return False
    if a == b == c :
        return True
    return False
    


def isosceles(sides):
    if not isvalide(sides) :
        return False
    a,b,c = sides
    if (a == 0) or (b==0) or (c==0):
        return False
    if ((a==b) or (b==c)) or (a==c):
        return True
    return False


def scalene(sides):
    if not isvalide(sides) :
        return False
    a,b,c = sides
    if (a == 0) or (b==0) or (c==0):
        return False
    if (a != b) and (b != c) and (a != c):
        return True
    return False
