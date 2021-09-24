
def verifica_cpf_primeiro_digito(cpf):
    j = 2
    soma_multi = 0
    for i in range(8, -1, -1):
        soma_multi += int(cpf[i])*j
        j += 1
    if soma_multi%11 < 2:
        digito = 0
    if soma_multi%11 >= 2:
        digito = 11-(soma_multi%11)
    if int(cpf[9]) != digito:
        return False
    return True

def verifica_cpf_segundo_digito(cpf):
    soma_multi = 0
    j = 2
    for f in range(9, -1, -1):
        soma_multi += int(cpf[f])*j
        j += 1
    if soma_multi%11 < 2:
        seg_digito = 0
    if soma_multi%11 >= 2:
        seg_digito = 11 - (soma_multi%11)
    if seg_digito == int(cpf[10]):
        return cpf
    return False

def tira_simbolos(cpf):
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    return cpf

#Esta é a função que chama as outras acima,
#primeiro tira os símbolos
#depois, verifica se a str cpf tem menos de 11 números
#confere o primeiro dígito, se esta retornar False, a verifica_cpf retorna False
#depois, retorna o resultado da função que verifica o segundo dígito. Ou seja, False, ou o cpf

def verifica_cpf(cpf):
    cpf = tira_simbolos(cpf)
    if len(cpf) < 11:
        return False
    elif verifica_cpf_primeiro_digito == False:
        return False
    else:
        return verifica_cpf_segundo_digito(cpf)