# João Victor da Silva Santos e Marcos Fabrício Bezerra Severo

import menus
import menusGerais
import Clinicas.clinicasController as clinicas
import Consultas.consultasController as consultas
import Funcionario.funcionarioController as funcionarios
import Medicos.medicoController as medicos
import Pacientes.pacienteController as pacientes


def start():
    while True:
        menusGerais.menuPrincipal()
        escolha = int(input("Escolha uma opção: "))
        match escolha:
            case 1:
                pacientes.main()
            case 2:
                consultas.main()
            case 3:
                medicos.main()
            case 4:
                funcionarios.main()
            case 5:
                clinicas.main()

start()