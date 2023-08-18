ativos = []

quantidade_ativos = int(input())

for codigo_ativo in range(quantidade_ativos):
    codigo_ativo = input()
    ativos.append(codigo_ativo)
    
ativos.sort()

for ativo in ativos:
    print(ativo)