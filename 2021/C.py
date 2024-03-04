x, y = list(map(int, input().split()))

if x > 0 and y > 0 and x != y:
    print(x, y)
    print(y, x)
    print(y, -x)
    print(x, -y)
    print(-x, -y)
    print(-y, -x)
    print(-y, x)
    print(-x, y)
else:
    print("ERROR")