# print("Hello")
# a = int(input("Введите первую переменную:"))
# b = int(input("Введите вторую переменную:"))
# s = a+b
# print("Сумма равна:", s)

# a = int(input("a="))
# b = int(input("b="))
# print(a, b)
# a, b = b, a
# print(a, b)
from math import *

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
pp = (a + b + c) / 2
s = sqrt(pp * (pp - a) * (pp - b) * (pp - c))
print("Площадь треугольника:", "{:7.2f}".format(s),sep="")

