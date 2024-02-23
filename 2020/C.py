d = {}

falta = []
nomes = set()

for i in range(int(input())):
    a, b = input().split(" e ")
    nomes.add(a)
    nomes.add(b)
    if a == "Saracura":
        d[b] = 1
    elif b == "Saracura":
        d[a] = 1
    else:
        falta.append(f"{a} {b}")

while True:
    ver = False
    
    for i in d:
        for j in falta:
            if i in j:
                p = j.split(i)[0][:-1] if j.split(i)[0] != "" else j.split(i)[1][1:]
                if p not in d:
                    d[p] = d[i] + 1
                    ver = True
            if ver:
                break
        if ver:
            break
    
    if not ver:
        break

for nome in nomes:
    if nome not in d and nome != "Saracura":
        d[nome] = 9999999999999999999
        
unsorted_lists = {}

for i in set(d.values()):
    unsorted_lists[i] = []

for i in d:
    unsorted_lists[d[i]].append(i)


for i in sorted(set(d.values())):
    for j in sorted(unsorted_lists[i]):
        if i == 9999999999999999999:
            print(f"{j}: infinito")
        else:
            print(f"{j}: {i}")
