menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
qtd_saque = 0
LIMITE_SAQUES = 3

while True:

    usuario = input(f"Qual operação você deseja realizar? {menu} ")

    if usuario == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!\n")

        else:
            print("Valor inválido. Tente novamente\n")

    elif usuario == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = qtd_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.\n")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtd_saque += 1
            print("Saque realizado com sucesso!\n")

        else:
            print("Operação falhou! O valor informado é inválido.\n")

    elif usuario == "e":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")

    elif usuario == "q":
        print("Até breve!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")