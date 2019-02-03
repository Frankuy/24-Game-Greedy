def solving(numbers):
    result = 0
    choosen_sorted_op = []
    numbers.sort(reverse = True)

    for n in numbers:
        if (result + int(n) <= 24) :
            result += int(n)
            choosen_sorted_op.append('+')
        else :
            result -= int(n)
            choosen_sorted_op.append('-') 
    return result