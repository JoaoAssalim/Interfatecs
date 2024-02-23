d = {}

for i in range(int(input())):
    a, b = input().split()
    if f"{a} E" in d:
        d[f"{a} E"] += 1
    else:
        d[f"{a} E"] = 1
    if f"{b} D" in d:
        d[f"{b} D" ] += 1
    else:
        d[f"{b} D" ] = 1

l = []

for i in d:
    if d[i] > 1:
        l.append(i)

l.sort(key=lambda x: int(x[:-2]))

for i in l:
    print(f"{i[:-2]} {i[-1]} {d[i]-1}")
    
if len(l) == 0:
    print("SEM TROCAS DESTA VEZ")