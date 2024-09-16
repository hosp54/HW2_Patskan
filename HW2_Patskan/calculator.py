# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Authors: Афанасьева, Кудашева, Пацкан, Шипунова

#Функция сложения
def addition(a, b):
    return a + b

#Функция деления
def division(a, b):
    if b == 0:
        return 'На ноль делить нельзя'
    else:
        return a / b

#Функция main

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
