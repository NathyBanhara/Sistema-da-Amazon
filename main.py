import validade_cpf
import validade_email
from produtos import produtos #from produtos import ...

#quando pagar, excluir os produtos do carrinho  ??? pedir sobre como funciona na SEGUNDAAAAA
#arrumar todos os erros de ValueError
#arrumar a checagem do limite, diz, "O valor ultrapassa 1000"
#arrumar corretor de cadastro que não envia mensagem de inválido
#fazer opção de voltar quando email, senha especial e coisas do tipo não estão corretos
#checar_senha_especial dá erro se recebe algo escrito na primeiro tentativa, checar outros e arrumar
#erros tbm tem esse problema
#corrigir o erro de se não tem nenhum cliente, não dar erro no login, mas redirecionar a pagina inicial
#mudar os nomes das funções option para o que faz = carrinho(), compras(), cadastro()...

#Class

class Cadastrar:  #mudar nome
    def __init__(self, nome ,sobrenome, email, senha, cpf, limite_credito):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.limite_credito = limite_credito
        self.compras = []
        self.total_de_gastos = 0

#Procurar Usuário
def procurar_usuario_por_email(main, email):
    for i in range(len(main)):
        if main[i].email == email:
            return i
    return -1

def procurar_usuario_por_nome(main, nome, sobrenome):
    for i in range(len(main)):
        if main[i].nome == nome and main[i].sobrenome == sobrenome:
            return i
    return -1

def procurar_usuario_por_cpf(main, cpf):
    for i in range(len(main)):
        if main[i].cpf == cpf:
            return i
    return -1

#Checar senha do Cadastro

def checar_senha(senha):
    try:
        senha_numeros = int(senha)
        if len(senha) < 6:
            return False
        return senha
    except ValueError: 
        return False

#Checar senha especial


def checar_senha_especial():
    while True:
        try:
            senha = int(input("Senha de acesso: "))    #Não está funcionando
            if senha == 123456:
                return senha
        except ValueError:
            print("Senha inválida!")
        else:
            print("Senha inválida!")


#Erros

def erros_com_int(mensagem_inicio, primeiro_valor, segundo_valor, mensagem_erro):
    while True:
        try:
            variavel = int(input(mensagem_inicio))
            if variavel >= primeiro_valor and variavel <= segundo_valor:
                return variavel
        except ValueError:
            print(mensagem_erro)
        else:
            print(mensagem_erro)

def erros_com_float(mensagem_inicio, primeiro_valor, segundo_valor, mensagem_erro):
    while True:
        try:
            variavel = float(input(mensagem_inicio))
            if variavel >= primeiro_valor and variavel <= segundo_valor:
                return variavel
        except ValueError:
            print(mensagem_erro)
        else:
            print(mensagem_erro)


#Options Página Inicial

def option1(main):
    checar_senha_especial()
    listar_ou_procurar = erros_com_int("1. Listar todos clientes\n2. Procurar Cliente\n",
    1, 2, "Opção Inválida!\n")
    if listar_ou_procurar == 1:
        for cliente in range(len(main)):
            print(f"Cliente {cliente+1}:\nNome: {main[cliente].nome}\nSobrenome: {main[cliente].sobrenome}\n")
    elif listar_ou_procurar == 2:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        achar_cliente = procurar_usuario_por_nome(main, nome, sobrenome)
        if achar_cliente == -1:
            print("\nCliente não existe.\n")
        else:
                                      #checar se não nem uma das opções
            oque_checar = erros_com_int("\n1. Dados Cadastrais\n2. Carrinho\n", 1, 2, "Opção Inválida!\n")
            if oque_checar == 1:
                print(f"\nNome: {main[achar_cliente].nome}\nSobrenome: {main[achar_cliente].sobrenome}")
                print(f"Email: {main[achar_cliente].email}\nSenha: {main[achar_cliente].senha}")
                print(f"CPF: {main[achar_cliente].cpf}\nLimite de crédito: {(main[achar_cliente].limite_credito):.2f}\n")
            elif oque_checar == 2:
                for compra in range(len(main[achar_cliente].compras)):
                    print(f"\n{compra+1}. {main[achar_cliente].compras[compra][1]} - {main[achar_cliente].compras[compra][0]} - R$ {(main[achar_cliente].compras[compra][2]):.2f}\n")


def option2(main):
    nome = input("Primeiro nome: ") #Fazer algo para procurar pessoas repetidas
    sobrenome = input("Sobrenome: ")
    while True:
        email = validade_email.verifica_email(input("Email: "))
        if email != False:
            break
    senha = checar_senha(input("Senha (6 dígitos): ")) 
    while senha == False:
        print("Senha inválida!")
        senha = checar_senha(input("Senha (6 dígitos): "))
    while True:
        cpf = validade_cpf.verifica_cpf(input("CPF: ")) #ver se já tem pessoa com cpf
        if cpf != False:
            break
    limite_credito = erros_com_float("Limite de crédito: ", 12.00, 1000.00, 
    "Valor inválido. Por favor, escolha um valor entre R$ 12.00 e R$ 1000.00.")
    if procurar_usuario_por_nome(main, nome, sobrenome) != -1 or procurar_usuario_por_email(main, email) != -1 or procurar_usuario_por_cpf(main, cpf) != -1:
        print("O usuário já existe.")
        return 0
    else:
        person = Cadastrar(nome, sobrenome, email, senha, cpf, limite_credito)
        return person

def option3(main):
    email = procurar_usuario_por_email(main, input("\nEmail: "))
    tentativas_email = 1
    senha = input("Senha: ")
    retornar = False
    while email == -1 and tentativas_email <= 2:
        print("\nEmail inválido. Tente novamente.")
        email = procurar_usuario_por_email(main, input("Email: "))
        tentativas_email += 1
        if tentativas_email == 3 and email == -1:
            print("\nVocê excedeu o número de tentativas e será redirecionado à Pagina Inicial.\n")
            retornar = True
    if retornar == True:
        return -1
    tentativas_senha = 1
    while main[email].senha != senha and tentativas_senha <= 2:
        print("\nSenha inválida.")
        senha = input("Senha: ")
        tentativas_senha += 1
        if tentativas_senha == 3 and main[email].senha != senha:
            print("\nVocê excedeu o número de tentativas e será redirecionado à Pagina Inicial.\n")
            return -1
    return email

#Options Menu Principal    

def option_menu1(main, lista_de_produtos, usuario_atual):
    print("\nLista de Produtos:\n")
    for item in range(len(lista_de_produtos)):
        print(f"{item+1}. {lista_de_produtos[item].titulo} - R$ {(lista_de_produtos[item].valor):.2f}")
    print("\nEscolha os produtos que desejas comprar.\n")
    while True:
        compra = erros_com_int("Escreva o código do produto que desejas comprar: ", 
        1, 20, "Opção inválida.\n")
        quantidade = int(input("Quantidade: "))   #checar se quantidade é maior do que 0 e se não é int, corrigir
        if main[usuario_atual].limite_credito - (lista_de_produtos[compra-1].valor*quantidade) < 0:
            print("Você não possui crédito suficiente para realizar esta compra. Efetue o pagamento de sua conta.") #fazer algo para ir direto ao pagamento da fatura
        else:
            for quant in range(quantidade):
                main[usuario_atual].limite_credito -= lista_de_produtos[compra-1].valor
                main[usuario_atual].compras.append([lista_de_produtos[compra-1].tipo, lista_de_produtos[compra-1].titulo, 
                lista_de_produtos[compra-1].valor])
                main[usuario_atual].total_de_gastos += lista_de_produtos[compra-1].valor
        continuar = input("Continuar a comprar? (s- sim n-não) ")  #colocar para se ser diferente de "s"
        if continuar.lower() == "n":
            break  #tirar do limite #checar se está dentro dele

def option_menu2(main, lista_de_produtos, usuario_atual):
    print(f"Total de gastos: R$ {(main[usuario_atual].total_de_gastos):.2f}")
    ver_itens = erros_com_int("1. Listar todos os itens\n2. Sair\n", 1, 2, 
    "Opção Inválida!\n")
    if ver_itens == 2:
        print("Você escolheu sair do Carrinho.\n")
    else:
        # falar se está vazia
        for item in range(len(main[usuario_atual].compras)):
            print(f"{item+1}. {main[usuario_atual].compras[item][1]} - {main[usuario_atual].compras[item][0]} - R$ {(main[usuario_atual].compras[item][2]):.2f}")

def option_menu3(main, usuario_atual):
    valor_pagar = float(input("Valor que desejas pagar: "))  #checar se é um valor inválido, menor que 0  e se é uma str
    while main[usuario_atual].limite_credito + valor_pagar > 1000:
        print("Valor inválido. O valor ultrapassa R$ 1000.00.")
        valor_pagar = float(input("Valor que desejas pagar: "))
    main[usuario_atual].limite_credito += valor_pagar
    print(f"O valor foi inserido com sucesso. Seu crédito atual é de R$ {(main[usuario_atual].limite_credito):.2f}.")

main = []

lista_de_produtos = []
produtos(lista_de_produtos)

lista_compras = []

while True:
    option = erros_com_int("\nPágina Inicial\n\n1-Todos Clientes\n2-Cadastro\n3-Login\n4-Sair\n", 1, 4, 
    "Opção Inválida!\n")
    if option == 4:
        print("\nVocê escolheu a opção 4. A sessão será encerrada.")
        break
    else:   #tem que tirar a opção de ir direta ao login após
        if option == 1:   #pedir uma senha para poder acessar os dados
            option1(main)
            continue
        elif option == 2:
            novo = option2(main)
            if novo == 0:
                continue
            else:
                main.append(novo)
                usuario_atual = procurar_usuario_por_email(main, novo.email)
        elif option == 3:
            usuario_atual = option3()
            if usuario_atual == -1:
                continue
        while True:
            print(f"\n{main[usuario_atual].nome}, bem-vindo(a) ao Sistema da AmazonCC!\n\n")
            option_menu = erros_com_int("Menu Principal:\n\n1-Comprar\n2-Carrinho\n3-Pagar conta\n4-Sair\n", 1, 4, "Opção inválida.\n")
            if option_menu == 4:
                print("\nVocê escolheu a opção 4. Redirecionando-o à Página Principal.\n")
                break
            else:
                if option_menu == 1:
                    option_menu1(main, lista_de_produtos, usuario_atual)
                if option_menu == 2:
                    option_menu2(main, lista_de_produtos, usuario_atual)
                if option_menu == 3:
                    option_menu3(main, usuario_atual)
               