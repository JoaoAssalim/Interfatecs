def formatNames(name):
    name = name.split()
    
    if len(name) <= 2:
        return " ".join(name)
    
    for i in range(1, len(name)-1):
        name[i] = f"{name[i][0]}."
    
    return " ".join(name)


names = []

while True:
    try:
        name = input()
        names.append(name)
        
    except EOFError:
        break

names.sort()
        
for i in names:
    print(formatNames(i))