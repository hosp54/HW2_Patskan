# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Authors: Афанасьева, Кудашева, Пацкан, Шипунова


#Функция сложения
def addition(a, b):
    return a + b

#Функция вычитания
def subtraction(a, b):
    return a - b

#Функция умножения:
def multiplication(a, b):
    res = a * b
    return res

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


print('''Добро пожаловать в калькулятор. Введите строку в таком виде: "5 + 9". 
Чтобы закончить работу с калькулятором, введите "стоп".''')      
main() #вызов функции main, которая внутри себя уже зациклена до слова стоп

