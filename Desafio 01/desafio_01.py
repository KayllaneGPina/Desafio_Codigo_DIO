saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

    
def saldo_conta(saldo_atual, valor_deposito, valor_retirada) :
    deposito = saldo_atual + valor_deposito
    saque = deposito - valor_retirada
    
    return saque

novo_saldo = saldo_conta(saldo_atual, valor_deposito, valor_retirada)
print(f'Saldo atualizado em conta: {novo_saldo:.1f}')