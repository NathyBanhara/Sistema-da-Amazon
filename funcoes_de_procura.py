#Procuram usuário por
#email
#nome e sobrenome
#cpf
#Se for encontrado, devolvem o índice dele em main
#Se não, -1


def email(main, email):
    for i in range(len(main)):
        if main[i].email == email:
            return i
    return -1

def nome(main, nome, sobrenome):
    for i in range(len(main)):
        if main[i].nome == nome and main[i].sobrenome == sobrenome:
            return i
    return -1

def cpf(main, cpf):
    for i in range(len(main)):
        if main[i].cpf == cpf:
            return i
    return -1