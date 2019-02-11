def difference(result) :
     return abs(eval(result) - 24)

def solving(numbers):
    op_counter = 3
    operator = []
    point = 0
    numbers.sort(reverse = True)
    result = str(numbers[0])
    del numbers[0]
    
    while (difference(result) != 0) and (op_counter != 0):
        diff_temp = 0
        op_temp = ''
        for n in numbers:
            diff_temp = difference(result + '+' + str(n))
            op_temp = '+'
            if difference(result + '*' + str(n)) < diff_temp:
                diff_temp = difference(result + '*' + str(n))
                op_temp = '*'
            if difference(result + '-' + str(n)) < diff_temp:
                diff_temp = difference(result + '-' + str(n))
                op_temp = '-'
            if difference(result + '/' + str(n)) < diff_temp:
                diff_temp = difference(result + '/' + str(n))
                op_temp = '/'
            result = result + op_temp + str(n)
            operator.append(op_temp)
            op_counter -= 1

    result = result + '=' + str(eval(result))

    return result