'''7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.'''


def first(n):
    if n == 1:
        return n
    elif n > 0:
        return n + first(n-1)


def second(n):
    return n * (n + 1) // 2


n = 1

while True:
    if first(n) == second(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')
        break
    n += 1
