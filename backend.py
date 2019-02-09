# def operating(result, numbers, idx) :
#     if (idx == 0) :
#         result = result + '+' + str(numbers[idx])
#     elif (idx == 1) :
#         result = result + '-' + str(numbers[idx])
#     elif (idx == 2) :
#         result = result + '*' + str(numbers[idx])
#     elif (idx == 3) :
#         result = result + '/' + str(numbers[idx])

# bool lessThan(result) :
#     return (eval(result) < 24)

# bool moreThan(result) :
#     return (eval(result) > 24)

def difference(result) :
     return abs(eval(result) - 24)

def solving(numbers):
    op_counter = 3
    operator = []
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
            elif difference(result + '-' + str(n)) < diff_temp:
                diff_temp = difference(result + '-' + str(n))
                op_temp = '-'
            elif difference(result + '/' + str(n)) < diff_temp:
                diff_temp = difference(result + '/' + str(n))
                op_temp = '/'
            result = result + op_temp + str(n)
            operator.append(op_temp)
            op_counter -= 1
            
    # counter = 3
    
    # while not(equal(result)) and (counter != 0) :
    #     if lessThan(result) :
    #         operating(result, numbers, 0)
    #         counter -= 1
    #     if moreThan(result) :
    #         operating(result, numbers, 1)
    #         counter -= 1


    # for n in numbers:
    #     if (result + int(n) <= 24) :
    #         result += int(n)
    #         choosen_sorted_op.append('+')
    #     else :
    #         result -= int(n)
    #         choosen_sorted_op.append('-') 
    return result