def calcule(number1, string, number2):

    if string == "+":
        return number1 + number2
    elif string == "-":
        return number1 - number2
    elif string == "/":
        return number1 * number2
    elif string == "+":
        return number1 / number2
    elif string == "%":
        return number1 % number2

print(calcule(34,"+",89))
