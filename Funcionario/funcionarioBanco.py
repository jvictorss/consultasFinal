import json


def atualizaBanco():
    with open("./Funcionario/funcionarioBanco.json", 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarMatricula(matricula):
    with open("./Funcionario/funcionarioBanco.json", 'w') as fp:
        dados = json.load(fp)
    return dados.get(matricula)


def checkMatricula(matricula):
    banco = atualizaBanco()
    if matricula in banco:
        return True


def adicionar(funcionario):
    try:
        banco = atualizaBanco()
        banco[funcionario.get('crm')] = funcionario
        with open("./Funcionario/funcionarioBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


def altera(matricula, nome, email, telefone, endereco):
    try:
        banco = atualizaBanco()
        funcionario = banco.get(str(matricula))
        funcionario['nome'] = nome
        funcionario['email'] = email
        funcionario['telefone'] = telefone
        funcionario['endereco'] = endereco
        banco[matricula] = funcionario
        with open("./Funcionario/funcionarioBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
        return f"O Funcionário da matrícula {matricula} foi alterado com sucesso"
    except:
        print("Ocorreu um erro ao tentar alterar, tente novamente.")


def remover(matricula):
    try:
        banco = atualizaBanco()
        banco.pop(matricula)
        with open("./Funcionario/funcionarioBanco.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Ocorreu um erro, tente novamente.")


def pegarTodos():
    banco = atualizaBanco()
    return banco.values()
