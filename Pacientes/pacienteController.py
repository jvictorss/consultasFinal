import menusGerais
from Pacientes import pacienteBanco as banco
from Pacientes.pacienteBanco import *


def main():
    print("")
    menusGerais.menuPaciente()
    escolha = int(input("Selecione uma opção: "))
    match escolha:
        case 1:
            cadastrarPaciente()
        case 2:
            buscarPacienteCpf()
        case 3:
            editarPaciente()
        case 4:
            removerPaciente()
        case 5:
            listarTodosPacientes()
        case 6:
            print("\n...  Saindo do Menu de Paciente  ...\n... Voltando para o Menu Principal ...")
    linha2()


def cadastrarPaciente():
    print("=" * 30)
    cpf = input("Digite o CPF: ")
    nome = input("Insira o nome do Paciente: ")
    email = input("Insira o e-mail do paciente: ")
    telefone = input('Insira o telefone do paciente: ')
    endereco = input('Insira o endereco do paciente: ')

    banco.adicionar({'cpf': cpf, 'nome': nome, 'email': email, 'telefone': telefone, 'endereco': endereco})

    while True:
        escolha = str(input("Deseja adicionar mais um Paciente? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")
    main()


def buscarPacienteCpf():
    print("=" * 30)
    while True:
        cpf = input("Insira o CPF: ")
        resultado = banco.pegarCPF(cpf)
        if len(resultado) > 0:
            print(f'''
            Nome: {resultado.get('nome')}
            CPF: {resultado.get('cpf')}
            Email: {resultado.get('email')}
            Telefone: {resultado.get('telefone')}
            Endereço: {resultado.get('endereco')}
            ''')
            print("=" * 30)
            break
        else:
            print("CPF não encontrado, Digite novamente.")
            print("-" * 30)
    main()


def editarPaciente():
    print("=" * 30)
    while True:
        cpf = input("Insira o CPF do Paciente: ")
        if banco.checkCPF(cpf):
            nome = str(input("Qual o novo nome? "))
            email = input("Insira o novo email: ")
            telefone = input("Insira o novo telefone: ")
            endereco = input("Insira o novo endereço: ")
            print(banco.altera(cpf, nome, email, telefone, endereco))
            print("-" * 30)
            break
        else:
            print("O cpf não está cadastrado.")
            print("-" * 30)
    main()


def removerPaciente():
    print("-" * 30)
    cpf = input("Qual o CPF do Paciente? ")
    if banco.checkCPF(cpf):
        paciente = banco.pegarCPF(cpf)
        while True:
            escolha = int(input(f"Deseja realmente excluir {paciente.get('name')}?\n[1]- Sim \n[2]- Não \n:   "))
            if escolha == 1:
                banco.remover(cpf)
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
        print("O cpf não está cadastrado.")
        print("-" * 30)
    main()


def listarTodosPacientes():
    print("-" * 30)
    pacientes = banco.pegarTodos()
    if len(pacientes) > 0:
        for paciente in pacientes:
            print(f'''
            Nome: {paciente.get('nome')}
            CPF: {paciente.get('cpf')}
            Email: {paciente.get('email')}
            Telefone: {paciente.get('telefone')}
            Endereço: {paciente.get('endereco')}
                   ''')
        print("-" * 30)
    else:
        print('Não há pacientes cadastrados.')
        print("=" * 30)
    main()


def linha1():
    print("=" * 60)


def linha2():
    print("-" * 60)


def opcaoInvalida():
    print("{:=^60}".format(" Digite uma opção válida! "))
