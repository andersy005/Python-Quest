def ourSum(lower, upper, margin = 0):
    
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0

    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

ourSum(1,10) 