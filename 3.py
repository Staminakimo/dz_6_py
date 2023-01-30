# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
def check_num(x, y):
    min_num = min(x, y)
    div = 1
    for el in range(2, min_num+1):
        if x % el == 0 and y % el == 0:
            div = el
            break
    return div == 1


def divider():
    for y in range(1, 12):
        for x in range(1, y):
            if check_num(x, y):
                print(f'{x}/{y}', end=' ')
        print()


divider()
