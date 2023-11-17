"""def print_pattern(row):
    for i in range(1, row + 1):
        print('*' * i)

    for i in range(row -1, 0, -1):
        print('*' *i)

    print (print_pattern(5))"""

for i in range(1,20):
    print('*' *(10-abs(10-i)))


for i in tuple(range(1, 6)) + tuple(range(4, 0, -1)):
    print('*+' *i)

for i in range(-3, 4):
    print('*-' *(4-abs(i)))

for i in range(1,10):
    print('*/' *min(i, 10 - i))

    