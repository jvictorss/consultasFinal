import menusGerais

from Clinicas import clinicasBanco as banco
from Clinicas.clinicasBanco import *


def main():
    print("")
    menusGerais.menuClinica()
    escolha = int(input("Selecione uma opção: "))
    match escolha:
        case 1:
            cadastrarClinica()
        case 2:
            buscarClinicaCNPJ()
        case 3:
            editarClinica()
        case 4:
            removerClinica()
        case 5:
            listarTodasClinicas()
        case 6:
            print("\n...  Saindo do Menu de Clínicas  ...\n... Voltando para o Menu Principal ...")
    linha2()


def cadastrarClinica():
    print("=" * 30)
    cnpj = input("Insira o CNPJ: ")
    nome = input("Insira o nome da Clínica: ")
    endereco = input('Insira o endereco da Clínica: ')

    banco.adicionar({'cnpj': cnpj, 'nome': nome, 'endereco': endereco})

    while True:
        escolha = str(input("Deseja adicionar mais uma Clínica? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")
    main()


def buscarClinicaCNPJ():
    print("=" * 30)
    while True:
        cnpj = input("Insira o CNPJ: ")
        resultado = banco.pegarCNPJ(cnpj)
        if len(resultado) > 0:
            print(f'''
            Nome: {resultado.get('nome')}
            CNPJ: {resultado.get('cnpj')}
            Endereço: {resultado.get('endereco')}
            ''')
            print("=" * 30)
            break
        else:
            print("CNPJ não encontrado, digite novamente.")
            print("-" * 30)
    main()


def editarClinica():
    print("=" * 30)
    while True:
        clinica = input("Insira o CNPJ da Clínica: ")
        if banco.checkCNPJ(clinica):
            nome = str(input("Insira o novo nome: "))
            endereco = input("Insira o novo endereço: ")
            print(banco.altera(nome, endereco))
            print("-" * 30)
            break
        else:
            print("O CNPJ não está cadastrado.")
            print("-" * 30)
    main()


def removerClinica():
    print("-" * 30)
    cnpj = input("Insira o CNPJ da Clínica: ")
    if banco.checkCNPJ(cnpj):
        clinica = banco.pegarCNPJ(cnpj)
        while True:
            escolha = int(input(f"Deseja realmente excluir {clinica.get('name')}?\n[1]- Sim \n[2]- Não \n:   "))
            if escolha == 1:
                banco.remover(clinica)
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


def listarTodasClinicas():
    print("-" * 30)
    clinicas = banco.pegarTodos()
    if clinicas:
        for clinica in clinicas:
            print(f'''
            Nome: {clinicas.get('nome')}
            CNPJ: {clinicas.get('cnpj')}
            Endereço: {clinicas.get('endereco')}
                   ''')
        print("-" * 30)
    else:
        print('Não há clínicas cadastradas.')
        print("=" * 30)
    main()


def linha1():
    print("=" * 60)


def linha2():
    print("-" * 60)


def opcaoInvalida():
    print("{:=^60}".format(" Digite uma opção válida! "))
