import json


def atualizaBanco():
    with open("./Pacientes/pacienteBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarCPF(cpf):
    with open("./Pacientes/pacienteBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados.get(cpf)


def checkCPF(cpf):
    banco = atualizaBanco()
    if cpf in banco:
        return True


def adicionar(paciente):
    try:
        banco = atualizaBanco()
        banco[paciente.get('cpf')] = paciente
        with open("./Pacientes/pacienteBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


def altera(cpf, nome, email, telefone, endereco):
    try:
        banco = atualizaBanco()
        paciente = banco.get(str(cpf))
        paciente['nome'] = nome
        paciente['email'] = email
        paciente['telefone'] = telefone
        paciente['endereco'] = endereco
        banco[cpf] = paciente
        with open("./Pacientes/pacienteBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
        return f"O Paciente do CPF {cpf} foi alterado com sucesso"
    except:
        print("Ocorreu um erro ao tentar alterar, tente novamente.")


def remover(cpf):
    try:
        banco = atualizaBanco()
        banco.pop(cpf)
        with open("./Pacientes/pacienteBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Ocorreu um erro, tente novamente.")


def pegarTodos():
    banco = atualizaBanco()
    return banco.values()
