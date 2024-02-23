from math import floor

while True:
    try:
        n = int(input())
        all_values = []
        mean = 0
        unique_values = {}
        
        for i in range(n):
            num = int(input())
            mean += num
            
            if num in unique_values:
                unique_values[num] += 1
            else:
                unique_values[num] = 1
            
            all_values.append(num)
        
        all_values.sort()
        unique_values = sorted(unique_values.items(), key=lambda x: x[1], reverse=True)
        
        moda = []
        maior = unique_values[0][1]
        
        for i in unique_values:
            if i[1] != maior:
                break
            moda.append(str(i[0]))
        
        moda.sort(key=lambda x: int(x))
        
        if n % 2:
            mediana = all_values[int(floor(n/2))]
        else:
            mediana = (all_values[int(floor(n/2))] + all_values[int(floor(n/2))-1]) / 2
        
        print(f"MODA={','.join(moda)}")
        print(f"MEDIA={(mean/n):.2f}")
        print(f"MEDIANA={(mediana):.2f}")
        
    except EOFError:
        break