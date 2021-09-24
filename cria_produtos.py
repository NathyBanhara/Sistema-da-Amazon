#Cadastrar produtos
class Produtos:
    def __init__(self, tipo, titulo, valor):
        self.tipo = tipo
        self.titulo = titulo
        self.valor = valor

lista_de_livros = ['Harry Potter e a Pedra Filosofal', 'Harry Potter e a Câmara Secreta', 
'Harry Potter e o Prisioneiro de Askaban', 
'Harry Potter e o Cálice de Fogo', 'Harry Potter e a Ordem da Fênix', 
'Harry Potter e o Enigma do Príncipe', 'Harry Potter e as Relíquias da Morte', 'Jogador Número 1',
'Legend', 'Prodigy', 'Champion']
lista_de_filmes = ['Animais Fantásticos e Onde Habitam', 'Animais Fantásticos: Os Crimes de Grindelwald', 
'O Chamado','This is it']
lista_de_series = ['The Walking Dead', 'Elementary', 'Naruto', 'Naruto Shippuden', 'The 100']

lista_de_produtos = []

#Adiciona os livros à lista_de_produtos, começando com um preco de R$ 20.00 e aumentando a cada um em 2 reais
def adiciona_livros(lista_de_produtos, livros):
    preco = 20.00
    for i in range(len(livros)):
        p = Produtos('Livros', livros[i], preco)
        lista_de_produtos.append(p)
        preco += 2.00

#Adiciona os fimes à lista_de_produtos, começando com um preço de R$ 12.00 e aumentando a cada um em 2.50 reais
def adiciona_filmes(lista_de_produtos, filmes):
    preco = 12.00
    for i in range(len(filmes)):
        p = Produtos('Filmes', filmes[i], preco)
        lista_de_produtos.append(p)
        preco += 2.50

#Adiciona as séries à lista_de_produtos, começando com um preço de R$ 100.00 e aumentando a cada um em 10.00 reais
def adiciona_series(lista_de_produtos, series):
    preco = 100.00
    for i in range(len(series)):
        p = Produtos('Séries', series[i], preco)
        lista_de_produtos.append(p)
        preco += 10.00

#Chama as funções acima, adicionando os livros, filmes e séries à lista_de_produtos
def produtos(lista_de_produtos):
    adiciona_livros(lista_de_produtos, lista_de_livros)
    adiciona_filmes(lista_de_produtos, lista_de_filmes)
    adiciona_series(lista_de_produtos, lista_de_series)