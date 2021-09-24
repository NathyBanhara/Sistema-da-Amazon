def checa_nome(nome):
    for i in nome:
        try:
            i = int(i)
        except ValueError:
            continue
        else:
            return False
    return True

