saldo_total = int(input())
valor_saque = int(input())
  
if saldo_total >= valor_saque:
    saldo = saldo_total - valor_saque
    print(f'Saque realizado com sucesso! Novo saldo: {saldo}')
else:
    print('Saldo insuficiente. Saque não realizado.')


