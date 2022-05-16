# João Victor da Silva Santos e Marcos Fabrício Bezerra Severo

# Definição da tela de menus:


def menuPrincipal():
    print("")
    print("{:=^60}".format(" MENU PRINCIPAL "))
    print("\t[ 1 ] Menu de Paciente")
    print("\t[ 2 ] Menu de Marcação de Consulta")
    print("\t[ 3 ] Menu de Médico")
    print("\t[ 4 ] Menu de Funcionário")
    print("\t[ 5 ] Menu de Clínica")
    print("\t[ 6 ] SAIR DO SISTEMA")
    linha2()


def menuPaciente():
    print("")
    print("{:=^60}".format(" MENU PACIENTE "))
    print("\t[ 1 ] Cadastrar Paciente")
    print("\t[ 2 ] Buscar Paciente por CPF")
    print("\t[ 3 ] Editar Paciente")
    print("\t[ 4 ] Remover Paciente")
    print("\t[ 5 ] Listar todos os Pacientes")
    print("\t[ 6 ] Voltar ao Menu Principal")
    linha2()


def menuConsulta():
    print("")
    print("{:=^60}".format(" MENU CONSULTA "))
    print("\t[ 1 ] Marcar Consulta")
    print("\t[ 2 ] Buscar Consulta por Paciente")
    print("\t[ 3 ] Editar Consulta")
    print("\t[ 4 ] Remover Consulta")
    print("\t[ 5 ] Listar Consultas")
    print("\t[ 6 ] Listar Consultas por Retorno")
    print("\t[ 7 ] Listar Consultas por Intervalo de Datas")
    print("\t[ 8 ] Voltar ao Menu Principal")
    linha2()


def menuMedico():
    print("")
    print("{:=^60}".format(" MENU MÉDICO "))
    print("\t[ 1 ] Cadastrar Médico")
    print("\t[ 2 ] Buscar Médico por CRM")
    print("\t[ 3 ] Editar Médico")  # :Antes buscar por CRM
    print("\t[ 4 ] Remover Médico")
    print("\t[ 5 ] Listar todos os Medicos")
    print("\t[ 6 ] Pesquisar Médico por Especialidade")
    print("\t[ 7 ] Voltar ao Menu Principal")
    linha2()


def menuFuncionario():
    print("")
    print("{:=^60}".format(" MENU FUNCIONÁRIO "))
    print("\t[ 1 ] Cadastrar Funcionário")
    print("\t[ 2 ] Buscar Funcionário por Matrícula")
    print("\t[ 3 ] Editar Funcionário")  # :Antes buscar por matrícula
    print("\t[ 4 ] Remover Funcionário")
    print("\t[ 5 ] Listar todas as Funcionários")
    print("\t[ 6 ] Voltar ao Menu Principal")
    linha2()


def menuClinica():
    print("")
    print("{:=^60}".format(" MENU CLÍNICA "))
    print("\t[ 1 ] Cadastrar Clínica")
    print("\t[ 2 ] Buscar Clínica por CNPJ")
    print("\t[ 3 ] Editar Clínica")
    print("\t[ 4 ] Remover Clínica")
    print("\t[ 5 ] Listar todas as Clínicas")
    print("\t[ 6 ] Voltar ao Menu Principal")
    linha2()


def linha1():
    print("=" * 60)


def linha2():
    print("-" * 60)


def opcaoInvalida():
    print("{:=^60}".format(" Digite uma opção válida! "))
