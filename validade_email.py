#Se encontrar "@" na str email, devolve o email, se não, False
def verifica_email(email):
    achou = False
    for i in range (len(email)):
        if email[i] == "@":
            return email
    return False


