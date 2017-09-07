def number(number1, number2, number3):
    return [x for x in range(number1, number2 + 1) if x % number3 == 0]

print(number(1,10,2))
