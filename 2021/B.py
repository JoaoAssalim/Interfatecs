for i in range(int(input())):
    A, B, C = 0, 0, 0
    res = ""
    s = input()
    
    for i in s:
        if i == "A":
            if A == 0:
                res += 'D'
                A = 1
            else:
                if B == 0:
                    res += "D"
                    A = 0
                    B = 1
                else:
                    res += 'E'
                    A = 0
                    B = 0
        elif i == "B":
            if B == 0:
                res += 'D'
                B = 1
            else:
                res += 'E'
                B = 0
        else:
            if C == 0:
                C = 1
                
                if B == 0:
                    B = 1
                    res += "D"
                else:
                    B = 0
                    res += 'E'
            else:
                res += "E"
                C = 0
    print(res)