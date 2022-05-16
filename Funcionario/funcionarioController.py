import menusGerais
from Funcionario import funcionarioBanco as banco
from Funcionario.funcionarioBanco import *


def main():
    print("")
    menusGerais.menuFuncionario()
    escolha = int(input("Selecione uma opção: "))
    match escolha:
        case 1:
            cadastrarFuncionario()
        case 2:
            buscarFuncionarioMatricula()
        case 3:
            editarFuncionario()
        case 4:
            removerFuncionario()
        case 5:
            listarTodosFuncionarios()
        case 6:
            print("\n...  Saindo do Menu de Paciente  ...\n... Voltando para o Menu Principal ...")
    linha2()


def cadastrarFuncionario():
    print("=" * 30)
    matricula = input("Insira a matrícula: ")
    cpf = input("Insira o CPF: ")
    nome = input("Insira o nome do Funcionário: ")
    email = input("Insira o e-mail do Funcionário: ")
    telefone = input('Insira o telefone do Funcionário: ')
    endereco = input('Insira o endereco do Funcionário: ')

    banco.adicionar({'matricula': matricula, 'cpf': cpf, 'nome': nome, 'email': email, 'telefone': telefone, 'endereco': endereco})

    while True:
        escolha = str(input("Deseja adicionar mais um Funcionário? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")
    main()


def buscarFuncionarioMatricula():
    print("=" * 30)
    while True:
        matricula = input("Insira a matrícula: ")
        resultado = banco.pegarMatricula(matricula)
        if len(resultado) > 0:
            print(f'''
            Nome: {resultado.get('nome')}
            Matrícula: {resultado.get('matricula')}
            CPF: {resultado.get('cpf')}
            Email: {resultado.get('email')}
            Telefone: {resultado.get('telefone')}
            Endereço: {resultado.get('endereco')}
            ''')
            print("=" * 30)
            break
        else:
            print("Matrícula não encontrada, digite novamente.")
            print("-" * 30)
    main()


def editarFuncionario():
    print("=" * 30)
    while True:
        matricula = input("Insira a matrícula do Funcionário: ")
        if banco.checkMatricula(matricula):
            nome = str(input("Qual o novo nome? "))
            email = input("Insira o novo email: ")
            telefone = input("Insira o novo telefone: ")
            endereco = input("Insira o novo endereço: ")
            print(banco.altera(matricula, nome, email, telefone, endereco))
            print("-" * 30)
            break
        else:
            print("A matrícula não está cadastrada.")
            print("-" * 30)
    main()


def removerFuncionario():
    print("-" * 30)
    matricula = input("Qual a matrícula do Funcionário? ")
    if banco.checkMatricula(matricula):
        funcionario = banco.pegarMatricula(matricula)
        while True:
            escolha = int(input(f"Deseja realmente excluir {funcionario.get('name')}?\n[1]- Sim \n[2]- Não \n:   "))
            if escolha == 1:
                banco.remover(matricula)
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
        print("A matrícula não está cadastrada.")
        print("-" * 30)
    main()


def listarTodosFuncionarios():
    print("-" * 30)
    funcionarios = banco.pegarTodos()
    if len(funcionarios) > 0:
        for funcionario in funcionarios:
            print(f'''
            Nome: {funcionario.get('nome')}
            Matrícula: {funcionario.get('matricula')}
            CPF: {funcionario.get('matricula')}
            Email: {funcionario.get('email')}
            Telefone: {funcionario.get('telefone')}
            Endereço: {funcionario.get('endereco')}
                   ''')
        print("-" * 30)
    else:
        print('Não há funcionários cadastrados.')
        print("=" * 30)
    main()


def linha1():
    print("=" * 60)


def linha2():
    print("-" * 60)


def opcaoInvalida():
    print("{:=^60}".format(" Digite uma opção válida! "))
