t1 = {}
t2 = {}
f = {}

while True:
    try:
        nome, a, b, c = input().split()
        t1[f"{a} {nome}"] = nome
        t2[f"{b} {nome}"] = nome
        f[f"{c} {nome}"] = nome
        
    except EOFError:
        break

t1 = sorted(t1.items())[:3]
t1 = [i[1] for i in t1]
print(f"T1 {' '.join(t1)}")

t2 = sorted(t2.items())[:3]
t2 = [i[1] for i in t2]
print(f"T2 {' '.join(t2)}")

f = sorted(f.items())[:3]
f = [i[1] for i in f]
print(f"CHEGADA {' '.join(f)}")