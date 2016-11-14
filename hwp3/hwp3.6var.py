a = []
for i in range(7):
    a.append(int(input('Enter a number: ')))
for i in range(7):
    if a[i] > 0:
        print('X' * a[i])
    else:
        print()
