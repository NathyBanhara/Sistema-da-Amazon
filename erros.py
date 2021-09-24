#Recebe um valor, se ele não for int ou se não estiver entre ou incluindo o primeiro_valor ou o segundo_valor, reporta mensagem_erro
#só para quando as condições estiverem certas
def entre_com_int(mensagem_inicio, primeiro_valor, segundo_valor, mensagem_erro):
    while True:
        try:
            variavel = int(input(mensagem_inicio))
            if variavel >= primeiro_valor and variavel <= segundo_valor:
                return variavel
        except ValueError:
            print(mensagem_erro)
        else:
            print(mensagem_erro)

