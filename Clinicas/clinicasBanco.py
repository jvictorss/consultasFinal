import json


def atualizaBanco():
    with open("./Clinicas/clinicasBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarCNPJ(cnpj):
    with open("./Clinicas/clinicasBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados.get(cnpj)


def checkCNPJ(cnpj):
    banco = atualizaBanco()
    if cnpj in banco:
        return True


def adicionar(clinica):
    try:
        banco = atualizaBanco()
        banco[clinica.get('cnpj')] = clinica
        with open("./Clinicas/clinicasBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


def altera(cnpj, nome, endereco):
    try:
        banco = atualizaBanco()
        clinica = banco.get(str(cnpj))
        clinica['nome'] = nome
        clinica['endereco'] = endereco
        banco[cnpj] = clinica
        with open("./Clinicas/clinicasBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
        return f"A Clínica do CNPJ {cnpj} foi alterado com sucesso"
    except:
        print("Ocorreu um erro ao tentar alterar, tente novamente.")


def remover(cnpj):
    try:
        banco = atualizaBanco()
        banco.pop(cnpj)
        with open("./Clinicas/clinicasBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Ocorreu um erro, tente novamente.")


def pegarTodos():
    banco = atualizaBanco()
    return banco.values()
