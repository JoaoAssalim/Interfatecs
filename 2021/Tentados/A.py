# Mesma resolução do Josephus, não sei de cabeça

def solve(arr, n):
    last = -1
    idx = n - 1
    
    removed = []
    
    
    while arr:
        if len(arr) == 1:
            print(arr[0])
            return
        
        if idx >= len(arr):
            idx -= len(arr)
        
        arr.pop(idx)
    
        idx += (n-1)
            
            
        

while True:
    try:
        a, b = list(map(int, input().split()))
        solve(list(range(1, a+1)), b)
    
    except EOFError:
        break