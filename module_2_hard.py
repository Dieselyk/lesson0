def password(number):
    p = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                p += str(i) + str(j)
    return p

print('Введите число: ')
print(password(int(input())))