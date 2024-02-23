while True:
    H, C, L = list(map(float, input().split()))
    if H == C == L == 0:
        break
    i = H * 100 / C
    
    if i <= 8.334 and L >= 0.80:
        print("PROJETO SIMPLES")
    else:
        print("PROJETO ESPECIAL")
    