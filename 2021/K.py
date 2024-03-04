a, b, c = list(map(int, input().split()))
qt_r = input()
ref = list(map(int, input().split()))

for i in range(int(input())):
    x, y = list(map(int, input().split()))
    if b != c:
        if b == x and y not in ref:
            b = y

if b == c:
    print("PROSSEGUIR")
else:
    print("ABORTAR")