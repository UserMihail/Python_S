# 2. Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

num = int(input())
if num % 2 != 0:
    print('error')
else:
    a = num // 6
    b = a
    c = (a + b) * 2
print('Петя сделал', (a), 'корабликов')
print('Катя сделала', (c), 'корабликов')
print('Сережа сделал', (b), 'корабликов')