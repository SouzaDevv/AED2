'''def busca_binaria(v, l):
    esquerda = 0
    direita = len(l)

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if v == l[meio]:
            return "Encontrado"
        elif v < l[meio]:
            direita = meio - 1
            return "Encontrado"
        else:
            esquerda = meio + 1
            return "Encontrado"
    return -1

print(busca_binaria(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))'''

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''1. (ENADE): Considere um algoritmo de busca sequencial que procura por um determinado valor em um vetor 
de tamanho n. Sobre a complexidade desse algoritmo, assinale a alternativa CORRETA: 
A. Melhor caso em tempo O(n) e pior caso em tempo O(n²). 
B. Melhor caso em tempo O(1) e pior caso em tempo O(n) --> A resposta é essa. 
C. Melhor caso e pior caso ambos O(log n). 
D. A complexidade independe de n (tempo constante, O(1)).'''

'''2.(TEÓRICA): Por que o algoritmo de busca binária exige que o vetor esteja ordenado previamente? O que 
poderia acontecer se tentássemos aplicar a busca binária em um conjunto de dados não ordenado? 
Resposta --> Por conta que pode ocorrer um erro, caso a pessoa queira achar o numero 5, e ele está por ultimo quando deveria estar no meio, isso pode fazer ele 
ser descartado sem querer'''


'''3.(PRÁTICA): Implemente a função busca_binaria de forma recursiva em Python. Ou seja, escreva uma versão 
da busca binária que chame a si própria recursivamente em vez de usar um loop while. A função deve receber 
como parâmetros o vetor ordenado, o valor alvo buscado, e opcionalmente os índices esq e dir delimitando o 
segmento de busca (ou você pode definir a função interna aninhada com esses parâmetros). Retorne o índice 
do alvo no vetor caso seja encontrado, ou -1 caso contrário.'''

def busca_binaria(lista, alvo, esq=0, dir=None):
    if dir is None:
        dir = len(lista) - 1

    if esq > dir:
        return -1

    meio = (esq + dir) // 2

    if lista[meio] == alvo:
        return meio

    elif lista[meio] > alvo:
        return busca_binaria(lista, alvo, esq, meio - 1)

    else:
        return busca_binaria(lista, alvo, meio + 1, dir)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = busca_binaria(lista, 7)

if resultado != -1:
    print(f"Encontrado na posição {resultado}")
else:
    print("Não encontrado")


'''4.(PRÁTICA): Considere uma lista Python de 1000 números inteiros já ordenados em ordem crescente. Escreva 
um pequeno programa que utilize tanto a busca sequencial quanto a busca binária para encontrar um 
determinado número nessa lista e conte o número de comparações feitas em cada método. Faça o teste com 
um número que não esteja presente na lista (para forçar o pior caso) e exiba na saída o total de comparações 
realizadas por cada método. (Dica: você pode modificar as funções de busca para incrementarem um contador 
global ou utilizar variáveis externas para contar as comparações.)'''

listaa = range(1, 1001)


def busca_sequencial(alvo, listaa):
    comp = 0

    for i in range(len(listaa)):
        comp += 1

        if listaa[i] == alvo:
            return i, comp

    return -1, comp


def busca_binaria(alvo, listaa, esq=0, dir=None, comps=0):
    if dir is None:
        dir = len(listaa) - 1

    if esq > dir:
        return -1, comps

    meio = (esq + dir) // 2
    comps += 1

    if listaa[meio] == alvo:
        return meio, comps

    elif listaa[meio] < alvo:
        return busca_binaria(alvo, listaa, meio + 1, dir, comps)

    else:
        return busca_binaria(alvo, listaa, esq, meio - 1, comps)


alvo = 1001

resultado_seq, comparacoes_seq = busca_sequencial(alvo, listaa)
resultado_bin, comparacoes_bin = busca_binaria(alvo, listaa)


print("Busca sequencial:")
print(f"Resultado: {resultado_seq}")
print(f"Comparações: {comparacoes_seq}")

print("\nBusca binária:")
print(f"Resultado: {resultado_bin}")
print(f"Comparações: {comparacoes_bin}")


'''Projeto 1: Busca Eficiente em um Catálogo de Produtos Online 

Contexto: Imagine que você está desenvolvendo a funcionalidade de busca para um site de e-commerce com 
um grande número de produtos. O catálogo de produtos é armazenado em uma lista, onde cada item é um 
dicionário contendo informações como nome, preço e descrição. Para otimizar a busca, o catálogo é mantido 
ordenado alfabeticamente pelo nome do produto. 

Problema: Os clientes precisam encontrar rapidamente informações sobre um produto específico digitando 
seu nome na barra de busca. Uma busca lenta pode levar à frustração e à perda de vendas. 

Indicação de como resolver: Implemente um sistema de busca que utilize a busca binária para localizar o 
produto no catálogo ordenado. Ao receber o nome do produto digitado pelo usuário, sua função deve realizar a 
busca binária na lista de produtos. Se o produto for encontrado, retorne suas informações (por exemplo, preço, 
descrição). Caso contrário, informe que o produto não foi encontrado.'''

produtos = [
    {"nome": "Cadeira", "preco": 150, "descricao": "Cadeira de escritório"},
    {"nome": "Celular", "preco": 1200, "descricao": "Smartphone 128GB"},
    {"nome": "Fone", "preco": 200, "descricao": "Fone Bluetooth"},
    {"nome": "Notebook", "preco": 3500, "descricao": "Notebook 16GB RAM"},
    {"nome": "Teclado", "preco": 150, "descricao": "Teclado mecânico"}
]

def buscar_produto(nome, produtos):
    esq = 0
    dir = len(produtos) - 1

    while esq <= dir:
        meio = (esq + dir) // 2

        if produtos[meio]["nome"] == nome:
            return produtos[meio]
        
        elif produtos[meio]["nome"] < nome:
            esq = meio + 1

        else:
            dir = meio - 1


    return 

nome = input("Digite o nome do produto: ")

produto = buscar_produto(nome, produtos)

if produto is not None:
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Descrição: {produto['descricao']}")
else:
    print("Produto não encontrado.")


'''Projeto 2: Busca Eficiente em um Índice de Livros 

Contexto: Você está trabalhando em um projeto para gerenciar uma biblioteca. As informações sobre os livros 
(título, autor, ano de publicação) estão armazenadas em uma lista, e essa lista é mantida ordenada 
alfabeticamente pelo título do livro. 

Problema: Os usuários precisam encontrar rapidamente um livro específico sabendo seu título. Uma busca 
ineficiente pode dificultar a localização dos livros desejados. 

Indicação de como resolver: Desenvolva uma funcionalidade que permita aos usuários buscar um livro pelo 
título utilizando a busca binária. Ao receber o título do livro, sua função deve procurar no índice ordenado. Se o 
livro for encontrado, exiba suas informações (título, autor, ano). Caso contrário, informe que o livro não foi 
encontrado.'''

livros = [
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943},
    {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "ano": 1813}
]


def buscar_livro(titulo, livros):
    esq = 0
    dir = len(livros) - 1

    while esq <= dir:
        meio = (esq + dir) // 2

        if livros[meio]["titulo"] == titulo:
            return livros[meio]

        elif livros[meio]["titulo"] < titulo:
            esq = meio + 1

        else:
            dir = meio - 1

    return None


titulo = input("Digite o título do livro: ")

livro = buscar_livro(titulo, livros)

if livro is not None:
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano: {livro['ano']}")
else:
    print("Livro não encontrado.")
