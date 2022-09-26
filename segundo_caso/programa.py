def validarAprovacao(idade, formacao):
    if (idade > 25) and (formacao in ["engenharia", "informatica"]):
        return True
    else:
        return False
