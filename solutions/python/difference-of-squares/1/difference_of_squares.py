def square_of_sum(number):
    list_number = []
    sum = 0
    square_of_sum = 0
    for i in range(1, number+1, 1) :
        list_number.append(i)
    for i in list_number :
        sum += i
        square_of_sum = sum ** 2
        

    return square_of_sum
           
def sum_of_squares(number):
    list_number = []
    sum = 0
    for i in range(1, number+1, 1) :
        list_number.append(i)
    for i in list_number :
        sum += i ** 2
    return sum


def difference_of_squares(number):
    square_of_sum_1 = square_of_sum(number)
    sum_of_squares_1 = sum_of_squares(number)

    return square_of_sum_1 - sum_of_squares_1
