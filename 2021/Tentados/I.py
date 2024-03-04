# Quase

def bfs(start, goal, graph, visited):
    queue = [start]
    
    while queue:
        x, y = queue.pop(0)
        
        if (x, y) == goal:
            return
        
        if (x, y) not in visited:
            visited.append((x, y))
            for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xn = x + i[0]
                yn = y + i[1]
                
                if xn >= 0 and xn < len(graph) and yn >= 0 and yn < len(graph[0]) and graph[xn][yn] == 1:
                    queue.append((xn, yn))


matrix = []
n = int(input())
start =  list(map(int, input().split()))
start = [i-1 for i in start]
goal = list(map(int, input().split()))
goal = [i-1 for i in goal]

for i in range(n):
    l = input()
    l = [int(i) for i in l]
    matrix.append(l)


visited = []

bfs(start, goal, matrix, visited)

visited = [(i[0]+1, i[1]+1) for i in visited]

for i in visited:
    print(i[0], i[1])