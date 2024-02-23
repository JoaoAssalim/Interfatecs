d = {}

x = int(input())
while True:
    try:
        n, m = list(map(int, input().split()))
        if n in d:
            d[n].append(m)
        else:
            d[n] = [m]
            
    except EOFError:
        break

a, b = set(), set()
ver = True

for i in d:
    if i in a:
        for j in d[i]:
            if j in a:
                ver = False
                break
        b.add(j)
        
    elif i in b:
        for j in d[i]:
            if j in b:
                ver = False
                break
        a.add(j)
        
    else:
        ver2 = True
        
        for j in d[i]:
            if j in a:
                ver = False
                break
        
        if not ver2:
            for j in d[i]:
                a.add(j)
            b.add(i)
        else:
            for j in d[i]:
                b.add(j)
            a.add(i)
        
if ver:
    print("FESTA!")
else:
    print("Lascou...")