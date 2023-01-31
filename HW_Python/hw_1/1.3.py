# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

print('Введиет билет: ')
n = int(input())

a = n % 10
b = n // 10 % 10
c = n // 100 % 10
d = n // 1000 % 10
e = n // 10000 % 10
f = n // 100000 % 10

if (a + b + c == d + e + f):
    print('yes')
else:
    print('no')