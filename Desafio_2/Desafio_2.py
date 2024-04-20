def menu():
    menu = """
    SELECIONE A OPÇÃO DESEJADA:

        [1] - Depositar;
        [2] - Sacar;
        [3] - Extrato;
        [4] - Criar Novo Usuário;
        [5] - Criar Nova Conta;
        [6] - Contas Existentes;
        [0] - Sair.

=> """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\nObrigado por usar nosso sistema bancário, Voltando ao MENU PRINCIPAL!\n")
    print("==========================================")    

def novo_usuario(usuario):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = confere_usuario_existe(cpf, usuario)

    if usuario_existente:
        print("\n Já existe um usuário com esse CPF!")
        return
    
    print("==========================================")    
    print("Criando usuário, insira as informações: ")
    nome = input("Nome Completo: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")
    

def confere_usuario_existe(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuario if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def contas_existentes(contas):
    for conta in contas:
            linha = f"""\
                Agência:    {conta['agencia']}
                C/C:        {conta['numero_conta']}
                Titular:    {conta['usuario']['nome']}
            """
            print("=" * 100)
            print((linha))

def  criar_nova_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do usuário: ")
    usuario = confere_usuario_existe(cpf, usuario)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saques = numero_saques > limite_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite

    if excedeu_saldo:
        print("\nOperação falhou! \nVocê não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! \nO valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! \nNúmero máximo de 3 saques diários excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("Operação falhou! O valor informado é inválido.")
            
    return saldo, extrato    
    
def main():
    
    limite = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    extrato = ""
    numero_saques = 0
    


    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
                   
        elif opcao == "2":            
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )
            numero_saques += 1  
                   
        elif opcao == "3":
            mostrar_extrato(saldo, extrato = extrato) 
                  
        elif opcao == "4":
            novo_usuario(usuario) 
                   
        elif opcao == "5":
            numero_conta = len(contas) + 1
            nova_conta = criar_nova_conta(AGENCIA, numero_conta, usuario)

            if nova_conta: 
                contas.append(nova_conta)
                    
        elif opcao == "6":
            contas_existentes(contas)
                    
        elif opcao == "0":
            print("\nObrigado por usar nosso sistema bancário, até logo!\n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
                
main()