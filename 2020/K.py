cell = {}

for i in range(12):
    l = input().split(";")
    cell[l[0]] = "".join(l[1:])

users = {}
tentativas = {}

while True:
    user, passw = input().split(";")
    
    if user == passw == "fim":
        break
    
    users[user] = passw
    tentativas[user] = 0

while True:
    try:
        info = input().split(";")
        user = info[0]
        senha = info[1:]
        
        if user in users:
            senha_correta = users[user]
            
            if tentativas[user] < 3:
            
                if len(senha_correta) != len(senha):
                    if tentativas[user] + 1 >= 3:
                        print(f"{user}: usuario bloqueado")
                    else:
                        print(f"{user}: acesso negado")
                    tentativas[user] += 1
                else:
                    ver = True
                    for i, s in enumerate(senha):
                        if not senha_correta[i] in cell[s]:
                            ver = False
                            break
                    
                    if ver:
                        print(f"{user}: acesso concedido")
                        tentativas[user] = 0
                    else:
                        if tentativas[user] + 1 >= 3:
                            print(f"{user}: usuario bloqueado")
                        else:
                            print(f"{user}: acesso negado")
                        tentativas[user] += 1
            else:
                print(f"{user}: usuario bloqueado")
                
        else:
            print(f"{user}: usuario inexistente")
            
        
    except EOFError:
        break
