# João Victor da Silva Santos e Marcos Fabrício Bezerra Severo

from Pacientes.pacienteController import cadastrarPaciente, buscarPacienteCpf, editarPaciente, removerPaciente, listarTodosPacientes
from Medicos.medicoController import *
from Funcionario.funcionarioController import *
from Consultas.consultasController import *
from Clinicas.clinicasController import *
from menusGerais import menuPrincipal, menuClinica, menuFuncionario, menuMedico, menuConsulta, menuPaciente, opcaoInvalida


# Início do sistema:
def iniciarSistema():
    while True:
        menuPrincipal()
        opcaoPrincipal = input("Digite o número da opção desejada: ")
        if opcaoPrincipal == "1":
            while True:
                menuPaciente()
                opcaoPaciente = input("Digite o número da opção desejada: ")
                if opcaoPaciente == "1":
                    cadastrarPaciente()
                elif opcaoPaciente == "2":
                    buscarPacienteCpf()
                elif opcaoPaciente == "3":
                    editarPaciente()
                elif opcaoPaciente == "4":
                    removerPaciente()
                elif opcaoPaciente == "5":
                    listarTodosPacientes()
                elif opcaoPaciente == "6":
                    print("\n...  Saindo do Menu de Paciente  ...\n... Voltando para o Menu Principal ...")
                    break
                else:
                    opcaoInvalida()
        elif opcaoPrincipal == "2":
            while True:
                menuConsulta()
                opcaoConsulta = input("Digite o número da opção desejada: ")
                if opcaoConsulta == "1":
                    marcarConsulta()
                elif opcaoConsulta == "2":
                    buscarConsultaPaciente()
                elif opcaoConsulta == "3":
                    editarConsulta()
                elif opcaoConsulta == "4":
                    removerConsulta()
                elif opcaoConsulta == "5":
                    listarConsultas()
                elif opcaoConsulta == "6":
                    listarConsultaRetorno()
                elif opcaoConsulta == "7":
                    listarConsultaIntervData()
                elif opcaoConsulta == "8":
                    print("\n...  Saindo do Menu de Marcação de Consulta  ...\n... Voltando para o Menu Principal ...")
                    break
                else:
                    opcaoInvalida()
        elif opcaoPrincipal == "3":
            while True:
                menuMedico()
                opcaoMedico = input("Digite o número da opção desejada: ")
                if opcaoMedico == "1":
                    cadastrarMedico()
                elif opcaoMedico == "2":
                    buscarMedicoCRM()
                elif opcaoMedico == "3":
                    editarMedico()
                elif opcaoMedico == "4":
                    removerMedico()
                elif opcaoMedico == "5":
                    listarTodosMedicos()
                elif opcaoMedico == "6":
                    pesquisarMedicoEspecialidade()
                elif opcaoMedico == "7":
                    print("\n...  Saindo do Menu de Médico  ...\n... Voltando para o Menu Principal ...")
                    break
                else:
                    opcaoInvalida()
        elif opcaoPrincipal == "4":
            while True:
                menuFuncionario()
                opcaoFuncionario = input("Digite o número da opção desejada: ")
                if opcaoFuncionario == "1":
                    cadastrarFuncionario()
                elif opcaoFuncionario == "2":
                    buscarFuncionarioMatricula()
                elif opcaoFuncionario == "3":
                    editarFuncionario()
                elif opcaoFuncionario == "4":
                    removerFuncionario()
                elif opcaoFuncionario == "5":
                    listarTodosFuncionarios()
                elif opcaoFuncionario == "6":
                    print("\n...  Saindo do Menu de Paciente  ...\n... Voltando para o Menu Principal ...")
                    break
                else:
                    opcaoInvalida()
        elif opcaoPrincipal == "5":
            while True:
                menuClinica()
                opcaoClinica = input("Digite o número da opção desejada: ")
                if opcaoClinica == "1":
                    cadastrarClinica()
                elif opcaoClinica == "2":
                    buscarClinicaCnpj()
                elif opcaoClinica == "3":
                    editarClinica()
                elif opcaoClinica == "4":
                    removerClinica()
                elif opcaoClinica == "5":
                    listarTodasClinicas()
                elif opcaoClinica == "6":
                    print("\n...  Saindo do Menu de Paciente  ...\n... Voltando para o Menu Principal ...")
                    break
                else:
                    opcaoInvalida()
        elif opcaoPrincipal == "6":
            print("")
            print("{:=^60}".format("  ... Saindo do Sistema ...  "))
            print("{:=^60}".format("  <<<   ATÉ A PRÓXIMA   >>>  "))
            break
        else:
            opcaoInvalida()


iniciarSistema()
