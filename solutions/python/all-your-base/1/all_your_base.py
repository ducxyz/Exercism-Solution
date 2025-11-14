def rebase(input_base, digits, output_base):
    if input_base < 2 :
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if digits == []:  
        return [0]

    while len(digits) > 1 and digits[0] == 0:
        digits = digits[1:]

    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    value = 0
    for d in digits:
        value = value * input_base + d

    if value == 0:
        return [0]

    result = []
    while value > 0:
        remainder = value % output_base
        result.append(remainder)
        value = value // output_base

    result.reverse()
    return result
