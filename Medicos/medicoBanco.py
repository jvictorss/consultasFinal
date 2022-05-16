import json


def atualizaBanco():
    with open("./Medicos/medicoBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarCRM(crm):
    with open("./Medicos/medicoBanco.json", 'w') as fp:
        dados = json.load(fp)
    return dados.get(crm)


def checkCRM(crm):
    banco = atualizaBanco()
    if crm in banco:
        return True


def adicionar(medico):
    try:
        banco = atualizaBanco()
        banco[medico.get('crm')] = medico
        with open("./Medicos/medicoBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


def altera(crm, nome, email, telefone, endereco):
    try:
        banco = atualizaBanco()
        medico = banco.get(str(crm))
        medico['nome'] = nome
        medico['email'] = email
        medico['telefone'] = telefone
        medico['endereco'] = endereco
        banco[crm] = medico
        with open("./Medicos/medicoBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
        return f"O Medico do CRM {crm} foi alterado com sucesso"
    except:
        print("Ocorreu um erro ao tentar alterar, tente novamente.")


def remover(crm):
    try:
        banco = atualizaBanco()
        banco.pop(crm)
        with open("./Medicos/medicoBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Ocorreu um erro, tente novamente.")


def pegarTodos():
    banco = atualizaBanco()
    return banco.values()
