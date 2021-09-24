import erros

#Quando escolhida a opção de filtrar a compra, na opção Comprar, 
#pede o tipo de filtragem que o usuário deseja, preço ou tipo,
#e conforme o que é escolhido, adiciona á lista mostrar_produtos
#os produtos que seguem o que foi filtrado, retornando essa lista

def filtro(lista_de_produtos):
    mostrar_produtos = []
    print("\nFiltro:\n1- Preço\n2- Tipo")
    opcao_principal = erros.entre_com_int("", 1, 2, "Opção inválida!")
    if opcao_principal == 1:
        print("\n1- Até R$ 100.00\n2- Acima de R$ 100.00")
        opcao_preco = erros.entre_com_int("", 1, 2, "Opção inválida!")
        if opcao_preco == 1:
            for p_menor in range(len(lista_de_produtos)):
                if lista_de_produtos[p_menor].valor <= 100.00:
                    mostrar_produtos.append(lista_de_produtos[p_menor])
        else:
            for p_maior in range(len(lista_de_produtos)):
                if lista_de_produtos[p_maior].valor > 100.00:
                    mostrar_produtos.append(lista_de_produtos[p_maior])
    elif opcao_principal == 2:
        print("\n1- Livros\n2- Filmes\n3- Séries")
        opcao_tipo = erros.entre_com_int("", 1, 3, "Opção inválida!")
        if opcao_tipo == 1:
            for livro in range(len(lista_de_produtos)):
                if lista_de_produtos[livro].tipo == "Livros":
                    mostrar_produtos.append(lista_de_produtos[livro])
        elif opcao_tipo == 2:
            for filme in range(len(lista_de_produtos)):
                if lista_de_produtos[filme].tipo == "Filmes":
                    mostrar_produtos.append(lista_de_produtos[filme])
        else:
            for serie in range(len(lista_de_produtos)):
                if lista_de_produtos[serie].tipo == "Séries":
                    mostrar_produtos.append(lista_de_produtos[serie])      
    return mostrar_produtos


