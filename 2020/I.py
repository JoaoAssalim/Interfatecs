a, b = list(map(int, input().split()))
vals = list(map(int, input().split()))
vals.sort()

x, y = 0, b

ver = True

while True:
    soma = sum(vals[x:y])
    if soma == a or a in vals:
        break
    elif soma > a:
        y -= 1
    elif soma < a:
        x += 1
    
    if y < x:
        ver = False
        break

if ver:
    print("SIM")
else:
    print("NAO")