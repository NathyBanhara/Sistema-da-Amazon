def verifica_email(email):
    achou = False
    for i in range (len(email)):
        if email[i] == "@":
            return email
    return False


