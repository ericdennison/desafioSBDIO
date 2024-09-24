

menu  = """
    Que transação deseja realizar?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair


    =====> """


deposito = 0
saldo = 0
total_saques = 0
extrato_depositado = []
extrato_sacado = []

while True: 

    opcao = input(menu)




    #DEPÓSITO
    if opcao == 'd':
        while True: 

            valor_depositado = int(input("Digite o valor para Depósito: "))
            if valor_depositado > 0:
                saldo += valor_depositado
                print(f"Valor depositado: {valor_depositado} R$")
                print(f"Seu saldo: {saldo} R$")
                extrato_depositado.append(valor_depositado)
            else:
                print("Depósito Inválido")

            resposta = input('Continuar deposito? [s]im [n]ão \n')

            if resposta == 's':
                continue
            elif resposta == 'n':
                break
        


    #SAQUE
    elif opcao == 's':

        while True: 
            
            if total_saques >=3:
                print("Você atingiu o total de saques por dia!")
                break

            valor_sacado = int(input("Digite o valor do Saque: "))
            if saldo == 0:
                print("Você não tem saldo suficiente!")
                break
            if valor_sacado > 0 and valor_sacado <= saldo:
                if valor_sacado <= 500 :
                    
                    if total_saques < 3:

                        saldo -= valor_sacado
                        print(f"Valor sacado: {valor_sacado}R$")
                        print(f"Saldo atual: {saldo}R$")
                        extrato_sacado.append(valor_sacado)
                        total_saques += 1

                        resposta = input('Continuar saque? [s]im [n]ão \n')
                        if resposta == 's':
                            continue
                        elif resposta == 'n':
                            break
                        
                    # elif total_saques >= 3:
                    #     print("Você atingiu o total de saques por dia!")
                    #     break
                else:
                    print("Valor muito alto seu limite de saque é 500 R$")

            else:
                print(f"Valor Sacado: {valor_sacado}R$ é maior que o seu Saldo: {saldo}R$")

                resposta = input('Continuar saque? [s]im [n]ão \n')

                if resposta == 's':
                    continue
                elif resposta == 'n':
                    break
        


    #EXTRATO 
    elif opcao  == 'e':
        for i in extrato_depositado:
            print(f"Valores Depositados: {i}R$")
        for i in extrato_sacado:
            print(f"Valores Sacados: {i}R$")

        print(f"Saldo atual: {saldo}R$ ")
        
        resposta = input('Voltar ao Menu? [s]im [n]ão \n')

        if resposta == 's':
            continue
        elif resposta == 'n':
            break
        


    #SAINDO
    elif opcao == 'q':
        print('Saindo')
        break



    #OPÇÃO INVÁLIDA 
    else:
        print('Opção Inválida')
        continue


