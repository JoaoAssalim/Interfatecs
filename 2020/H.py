from math import floor

vagas, part = list(map(int, input().split()))
votos = []

for i in range(part):
    votos.append(int(input()))

soma_votos = sum(votos)
quociente = int(round(soma_votos / vagas))

print(soma_votos, quociente)

par = {}
falta = vagas

for i in range(part):
    quoc_part = int(floor(votos[i] / quociente))
    par[f"Partido {i+1}"] = [votos[i], quoc_part]
    falta -= quoc_part


for i in range(falta):
    medias = []
    for j in par:
        if par[j][1] == 0:
            medias.append(0)
        else:
            conta = par[j][0] / (par[j][1] + 1)
            medias.append(conta)
    
    m = medias.index(max(medias))

    par[list(par.keys())[m]][1] += 1

for i in par:
    print(f"{i}: {par[i][1]}")