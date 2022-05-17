# João Victor da Silva Santos e Marcos Fabrício Bezerra Severo

import menusGerais
from Medicos import medicoBanco as banco
from Medicos.medicoBanco import *


def main():
    print("")
    menusGerais.menuMedico()
    escolha = int(input("Selecione uma opção: "))
    match escolha:
        case 1:
            cadastrarMedico()
        case 2:
            buscarMedicoCrm()
        case 3:
            editarMedico()
        case 4:
            removerMedico()
        case 5:
            listarTodosMedicos()
        case 6:
            print("\n...  Saindo do Menu de Paciente  ...\n... Voltando para o Menu Principal ...")
    linha2()


def cadastrarMedico():
    print("=" * 30)
    while True: 
        crm = input("Insira o CRM: ")
        checkCRM(crm)
        if (checkCRM == True):
            print(f"Já existe um cadastro do paciente {paciente.get('nome')} para o CPF {cpf}.")
            break
        cpf = input("Insira o CPF: ")
        nome = input("Insira o nome do Médico: ")
        email = input("Insira o e-mail do Médico: ")
        telefone = input('Insira o telefone do Médico: ')
        endereco = input('Insira o endereco do Médico: ')

        banco.adicionar({'crm': crm, 'cpf': cpf, 'nome': nome, 'email': email, 'telefone': telefone, 'endereco': endereco})

    while True:
        escolha = str(input("Deseja adicionar mais um Médico? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")
    main()


def buscarMedicoCrm():
    print("=" * 30)
    while True:
        crm = input("Insira o CRM: ")
        resultado = banco.pegarCRM(crm)
        if len(resultado) > 0:
            print(f'''
            Nome: {resultado.get('nome')}
            CRM: {resultado.get('crm')}
            Email: {resultado.get('email')}
            Telefone: {resultado.get('telefone')}
            Endereço: {resultado.get('endereco')}
            ''')
            print("=" * 30)
            break
        else:
            print("CRM não encontrado, Digite novamente.")
            print("-" * 30)
    main()


def editarMedico():
    print("=" * 30)
    while True:
        crm = input("Insira o CRM do Paciente: ")
        if banco.checkCRM(crm):
            nome = str(input("Qual o novo nome? "))
            email = input("Insira o novo email: ")
            telefone = input("Insira o novo telefone: ")
            endereco = input("Insira o novo endereço: ")
            print(banco.altera(crm, nome, email, telefone, endereco))
            print("-" * 30)
            break
        else:
            print("O crm não está cadastrado.")
            print("-" * 30)
    main()


def removerMedico():
    print("-" * 30)
    crm = input("Qual o CRM do Médico? ")
    if banco.checkCRM(crm):
        medico = banco.pegarCRM(crm)
        while True:
            escolha = int(input(f"Deseja realmente excluir {medico.get('name')}?\n[1]- Sim \n[2]- Não \n:   "))
            if escolha == 1:
                banco.remover(crm)
                print('Removido com sucesso.')
                print("-" * 30)
                break
            elif escolha == 2:
                print('Operação cancelada.')
                print("-" * 30)
                break
            else:
                print('Selecione uma opção válida')
                print("-" * 30)
    else:
        print("O crm não está cadastrado.")
        print("-" * 30)
    main()


def listarTodosMedicos():
    print("-" * 30)
    medicos = banco.pegarTodos()
    if len(medicos) > 0:
        for medico in medicos:
            print(f'''
            Nome: {medico.get('nome')}
            CRM: {medico.get('crm')}
            Email: {medico.get('email')}
            Telefone: {medico.get('telefone')}
            Endereço: {medico.get('endereco')}
                   ''')
        print("-" * 30)
    else:
        print('Não há médicos cadastrados.')
        print("=" * 30)
    main()


def linha1():
    print("=" * 60)


def linha2():
    print("-" * 60)


def opcaoInvalida():
    print("{:=^60}".format(" Digite uma opção válida! "))
