import menusGerais
from Pacientes import pacienteBanco as banco
from Pacientes.pacienteBanco import *

from Consultas.consultasBanco import validaData


def main():
    print("")
    menusGerais.menuConsulta()
    escolha = int(input("Selecione uma opção: "))
    match escolha:
        case 1:
            marcarConsulta()
        case 2:
            buscarConsultaPaciente()
        case 3:
            editarConsulta()
        case 4:
            removerConsulta()
        case 5:
            listarConsultas()
        case 6:
            listarConsultasRetorno()
        case 7:
            listarConsultasIntervalo()
        case 8:
            print("\n...  Saindo do Menu de Consultas  ...\n... Voltando para o Menu Principal ...")
    linha2()


def marcarConsulta():
    print("=" * 30)
    codigo = input("Digite o Código da consulta: ")
    paciente = input("Insira o nome do Paciente: ")
    medico = input("Insira o nome do Médico: ")
    data = input('Insira a data da consulta (dd/mm/aaaa): ')
    hora = input('Insira a hora da consulta (HH:MM):')
    # if validaData("%s %s".format(data, hora)):
    #   Continua normalmente
    # else: 
    #   Pede para inserir uma data válida
    
    retorno = input('Esta consulta dá direito a retorno? [S]/[N]: ')
    observacao = input('Insira a observacao, caso haja: ')

    banco.adicionar({'codigo': codigo, 'paciente': paciente, 'medico': medico, 'data': data, 'hora': hora, 'retorno': retorno, 'observacao': observacao})

    while True:
        escolha = str(input("Deseja adicionar mais uma Consulta? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")
    main()


def buscarConsultaPaciente():
    print("=" * 30)
    while True:
        paciente = input("Insira o nome do Paciente: ")
        resultado = banco.pegarPaciente(paciente)
        if len(resultado) > 0:
            print(f'''
            Paciente: {resultado.get('paciente')}
            Médico: {resultado.get('medico')}
            Data consulta: {resultado.get('data')}
            Hora consulta: {resultado.get('hora')}
            Retorno: {resultado.get('retorno')}
            Observação: {resultado.get('observacao')}
            ''')
            print("=" * 30)
            break
        else:
            print("Consulta não encontrada, digite novamente.")
            print("-" * 30)
    main()


def editarConsulta():
    print("=" * 30)
    while True:
        paciente = input("Insira nome do Paciente: ")
        if banco.checkPaciente(paciente):
            medico = input("Insira o nome do novo médico: ")
            data = input("Insira a nova data da consulta: ")
            hora = input("Insira a nova hora da consulta: ")
            print(banco.altera(paciente, medico, data, hora))
            print("-" * 30)
            break
        else:
            print("O paciente não tem consulta marcada.")
            print("-" * 30)
    main()


def removerConsulta():
    print("-" * 30)
    paciente = input("Qual o nome do Paciente? ")
    if banco.checkPaciente(paciente):
        paciente = banco.pegarPaciente(paciente)
        while True:
            escolha = int(input(f"Deseja realmente excluir a consulta de {paciente.get('paciente')}?\n[1]- Sim \n[2]- Não \n:   "))
            if escolha == 1:
                banco.remover(paciente)
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
        print("O paciente não tem consulta cadastrada.")
        print("-" * 30)
    main()


def listarConsultas():
    print("-" * 30)
    pacientes = banco.pegarTodos()
    if len(pacientes) > 0:
        for paciente in pacientes:
            print(f'''
            Paciente: {paciente.get('paciente')}
            Medico: {paciente.get('medico')}
            Data consulta: {paciente.get('data')}
            Hora consulta: {paciente.get('hora')}
            Retorno: {paciente.get('retorno')}
            Observação: {paciente.get('observacao')}
                   ''')
        print("-" * 30)
    else:
        print('Não há consultas cadastrados.')
        print("=" * 30)
    main()


def listarConsultasRetorno():
    return None


def listarConsultasIntervalo():
    return None


def linha1():
    print("=" * 60)


def linha2():
    print("-" * 60)


def opcaoInvalida():
    print("{:=^60}".format(" Digite uma opção válida! "))
