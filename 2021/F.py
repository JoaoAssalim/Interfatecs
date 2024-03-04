n = int(input())
x = 0
tipo = 0

for i in range(3, n+1, 2):

    if tipo == 0:
        conta = (i + i - 3) * 2
        x += conta
        tipo = 1
    else:
        tipo = 0

print(x)

