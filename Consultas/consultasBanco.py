import json


def atualizaBanco():
    with open("./Consultas/consultasBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarPaciente(paciente):
    with open("./Consultas/consultasBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados.get(paciente)


def checkPaciente(paciente):
    banco = atualizaBanco()
    if paciente in banco:
        return True


def adicionar(paciente):
    try:
        banco = atualizaBanco()
        banco[paciente.get('paciente')] = paciente
        with open("./Consultas/consultasBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


def altera(codigo, paciente, medico, data, hora, endereco):
    try:
        banco = atualizaBanco()
        paciente = banco.get(str(codigo))
        paciente['paciente'] = paciente
        paciente['medico'] = medico
        paciente['data'] = data
        paciente['hora'] = hora
        banco[codigo] = paciente
        with open("./Consultas/consultasBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
        return f"A consulta do paciente {paciente} foi alterada com sucesso"
    except:
        print("Ocorreu um erro ao tentar alterar, tente novamente.")


def remover(codigo):
    try:
        banco = atualizaBanco()
        banco.pop(codigo)
        with open("./Consultas/consultasBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Ocorreu um erro, tente novamente.")


def pegarTodos():
    banco = atualizaBanco()
    return banco.values()
