def main():

    elements = input().split()

    if elements == ['стоп']:
        return "Работа калькулятора завершена"
    else:
        elements[0] = float(elements[0])
        elements[2] = float(elements[2])
        if elements[1] == '/':
            res = division(elements[0], elements[2])
            print(res)
        elif elements[1] == '+':
            res = addition(elements[0], elements[2])
            print(res)   
        elif elements[1] == '*':
            res = multiplication(elements[0], elements[2])
            print(res)
        elif elements[1] == '-':
            res = subtraction(elements[0], elements[2])
            print(res)
        main()

