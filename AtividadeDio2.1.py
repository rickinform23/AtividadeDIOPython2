#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RICARDO
#
# Created:     11/07/2024
# Copyright:   (c) RICARDO 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def menu():
    menu_selecao = """
    Selecione as seguintes opções: Depósito[d], Saque[s], Extrato[e], Criar Conta nova[nc], Listar contas[lc], Criar novo usuário[cu], Sair[x]:
    => """
    return input(menu_selecao)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito feito!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo Insuficiente!")

    elif excedeu_limite:
        print("Valor do saque passou do limite!")

    elif excedeu_saques:
        print("Máximo de saques atingido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado!")

    else:
        print("Valor Inválido!!!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Número do CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já registrado!")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço completo: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        selecao = menu()

        if selecao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif selecao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif selecao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif selecao == "cu":
            criar_usuario(usuarios)

        elif selecao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif selecao == "lc":
            listar_contas(contas)

        elif selecao == "x":
            break

        else:
            print("Operação Inválida!")

main()
