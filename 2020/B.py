n, m = list(map(int, input().split()))

clusters = []

for i in range(n):
    x, y = list(map(int, input().split()))
    ver = False
    
    for j in range(len(clusters)):
        if abs(clusters[j][0] - x) + abs(clusters[j][1] - y) <= m:
            nx = int((clusters[j][0] + x) / 2)
            ny = int((clusters[j][1] + y) / 2)
            clusters[j] = (nx, ny)
            ver = True
            break
    
    if not ver:
        clusters.append((x, y))

print(len(clusters))
for i in clusters:
    print(i[0], i[1])