vagas = {i: "" for i in range(1, 16)}
qtd_vagas = 15

while True:
    try:
        s = input()
        soma = 0

        for i in s:
            soma += int(ord(i))

        pos = (soma % qtd_vagas) + 1

        if pos <= 15 and vagas[pos] == "" and pos > 0:
            vagas[pos] = s

    except EOFError:
        break
    
print(vagas)