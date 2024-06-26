import textwrap
def menu ():
    menu = """ \n
    ==== MENU =====
    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [nc] = Nova conta
    [lc] = Listar contas
    [nu] = Novo usuario
    [q] = Sair
    => """
    return input(textwrap.dedent(menu))




def deposito(saldo, valor, extrato, /):
      if valor > 0:
        saldo += valor
        extrato += f'Depósito: \t R${valor:.2f}\n'
        print('Depósito realizado com sucesso!') 
      else:
        print('Digite um valor válido')
      
      return saldo, extrato
def saque(*saldo, valor, extrato, limite,  numero_saques, limite_saques): 

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("Operação falhou. Saldo insuficiente")
        
        elif excedeu_limite:
            print("Operação falhou. Limite para saque foi excedido")
        
        elif excedeu_saques:
            print("Operação falhou. Numero para saques foi excedido")
        
        elif valor > 0 :
            saldo -= valor
            extrato == (f'Saque: R$ {valor:.2f}')
            numero_saques += 1
            print('Saque realizado com sucesso!')
        else:
            print('Digite um valor positivo!')

        return saldo, extrato
def gerar_extrato(saldo, /, *, extrato):
        if opcao == "e":
            print('------------------Extrato------------------')
            print('Não foram realizadas movimentações.' if not extrato else extrato)
            print(f'Saldo: R$ {saldo:.2f}')
            print('--------------------------------------------')
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(" Usuário não encontrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
        LIMITE_SAQUES = 4
        AGENCIA = '0001'

        saldo = 0 
        limite = 500
        extrato = " "
        numero_saques = 0
        usuarios = []
        contas = []

        while True:
            opcao = input(menu)

            if opcao == "d":
                valor = float(input('Informe o valor a ser depositado:'))

                saldo, extrato = deposito(saldo,valor, extrato)
        
            elif opcao == "s":
                valor = float(input('Informe o valor a ser sacado:'))

                saldo, extrato = saque(
                     saldo=saldo,
                     valor=valor,
                     extrato=extrato,
                     limite=limite,
                     numero_saques=numero_saques,
                     limite_saques=LIMITE_SAQUES,
                )
            elif opcao == "e":
                 gerar_extrato (saldo, extrato=extrato)
            elif opcao == "nu":
                 criar_usuario(usuarios)
            elif opcao == "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta: 
                    contas.append(conta)
            elif opcao == 'lc':
                 listar_contas(contas)
            elif opcao == 'q':
                 break
            
            else:
                print("Opção inválida, por favor selecione novamente a operação desejada.")
        

main()

