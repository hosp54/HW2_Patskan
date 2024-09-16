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

