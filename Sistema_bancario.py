#Criando um sistema bancário

conta = 1000
movimentacao = 0
saque = 3
deposito = 0
valor_max_saque = 0

while True:
    try:
        opcao_cliente = int(input('O que você deseja fazer?\n (1)Sacar\n (2)Depositar\n (3)Ver extrato\n (4)Sair\n Insira o número da opção desejada: '))
            
        if opcao_cliente == 1:
            if conta != 0:
                print("Saque.")
                print(f"VALOR MÍNIMO DO SAQUE: R$20,00\n")            
                valor_max_saque = float(input("Quanto você deseja sacar?\n "))
                while saque <= 3 :                     
                    if valor_max_saque <= 500:
                        saque = saque - 1
                        movimentacao = movimentacao + 1
                        print(f"Saque de R${valor_max_saque} realizado.")
                        break                    
                    else:
                        print("Saque não realizado. \nValor máximo permitido por saque é de R$500.")
                        break
                saldo_saque = conta - valor_max_saque
                print(f"Você possui {saque} saques disponíveis hoje.\n ")
            else:
                print("Saldo insuficiênte para saque.")

        elif opcao_cliente == 2:
            deposito = int(input("Depósito.\n Selecione o valor que deseja depositar: "))
            if deposito > 0 and deposito <= 100000:
                print(f"Depósito de R${deposito} realizado com sucesso.")
                movimentacao = movimentacao + 1
                saldo_deposito = conta + deposito
            else:
                print("Valor de depósito indisponível.\n ")

        elif opcao_cliente == 3:
                if movimentacao == 0:
                    print("Não houve movimentações na data de hoje.")
                else:
                    extrato = conta + deposito - valor_max_saque
                    print(f"Ver extrato.\n Você possui:\n R${extrato: .2f} em conta.\n {saque} saques disponíveis no dia de hoje.\n ")

        if opcao_cliente == 4:
            print("Sair.") 
            break             
        
    except ValueError as error:
        print(error)

