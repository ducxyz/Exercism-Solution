def largest_product(series, size):
    if size < 0:
        raise ValueError("span must not be negative")

    for i in series:
        if not i.isdigit():
            raise ValueError("digits input must only contain digits")

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if size == 0:
        return 1

    best = 0 

    for i in range(len(series) - size + 1):
        count = series[i:i+size]    
        product = 1
        for j in count:             
            product *= int(j)

        if product > best:
            best = product

    return best

