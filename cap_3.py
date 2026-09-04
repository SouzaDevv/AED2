1. (ENADE): Considere um algoritmo de busca sequencial que procura por um determinado valor em um vetor 
de tamanho n. Sobre a complexidade desse algoritmo, assinale a alternativa CORRETA: 
A. Melhor caso em tempo O(n) e pior caso em tempo O(n²). 
B. Melhor caso em tempo O(1) e pior caso em tempo O(n). 
C. Melhor caso e pior caso ambos O(log n). 
D. A complexidade independe de n (tempo constante, O(1)).

Resosta: B

###########################################################################################################################################################

2. (TEÓRICA): Suponha que você tenha uma lista não ordenada com 100 nomes e deseja verificar se o nome 
"Mariana" está presente. Sobre o algoritmo de busca sequencial nesse contexto, é correto afirmar que: 
A. No pior caso, será necessário comparar "Mariana" com todos os 100 nomes da lista. 
B. Caso "Mariana" não esteja na lista, o algoritmo irá interromper a busca na metade, por eficiência. 
C. Se "Mariana" estiver na primeira posição, ainda assim serão verificadas todas as 100 posições para 
confirmar duplicatas. 
D. A busca sequencial não funciona com listas de strings, apenas com números, devido às comparações.

Resposta = A 

##############################################################################################################################################################

3. (TEÓRICA): Considere a implementação clássica da busca sequencial que retorna o índice da primeira 
ocorrência do valor alvo ou -1 se não encontrar. Dada uma lista L = [7, 12, 5, 12, 8], se chamarmos a 
função busca_sequencial(12, L), qual será o resultado retornado? 
A. 1 
B. 2 
C. 3 
D. -1

Resposta = A


"Exercicio 4"

clientes = [
    "João",
    "Maria",
    "Carlos",
    "Ana",
    "Pedro",
    "Juliana",
    "Lucas",
    "Fernanda",
    "Rafael",
    "Beatriz"
]


def buscar_cliente(nome, clientes):

    for i in range(len(clientes)):
        if clientes[i] == nome:
            return i

    return -1


resultado = buscar_cliente("Carlos", clientes)

if resultado != -1:
    print(f"Cliente encontrado no índice {resultado}.")
else:
    print("Cliente não encontrado.")


resultado = buscar_cliente("Gustavo", clientes)

"Exercicio 5"

def conta_ocorrencias(valor, lista):
    contador = 0

    for elemento in lista:
        if elemento == valor:
            contador += 1

    return contador


# Casos de teste
print(conta_ocorrencias(3, [1, 3, 5, 3, 7]))  # 2
print(conta_ocorrencias(5, [5, 5, 2, 8, 5]))  # 3
print(conta_ocorrencias(10, [1, 2, 3, 4, 5])) # 0
print(conta_ocorrencias(2, [2, 2, 2, 2]))      # 4



"Exercicio 6"

def remove_elemento(lista, valor):
    if len(lista) == 0:
        return None

    for i in range(len(lista)):
        if lista[i] == valor:
            elemento_removido = lista[i]
            lista.pop(i)
            return elemento_removido

    return None


# Exemplo
lista = [10, 20, 30, 20, 40]

removido = remove_elemento(lista, 20)

print("Valor removido:", removido)
print("Lista após a remoção:", lista)

"Projeto 1"

filmes = [
    "Interestelar",
    "Vingadores: Ultimato",
    "O Senhor dos Anéis",
    "Homem-Aranha",
    "Batman: O Cavaleiro das Trevas"
]


def buscar_filme(titulo, lista):
    for i in range(len(lista)):
        if lista[i].lower() == titulo.lower():
            print(f"Filme encontrado: {lista[i]}")
            print(f"Posição (índice): {i}")
            return

    print("Filme não encontrado no catálogo.")


filme = input("Digite o título do filme que deseja buscar: ")

buscar_filme(filme, filmes)

"Projeto 2 "

convidados = [
    "João",
    "Maria",
    "Carlos",
    "Ana",
    "Pedro"
]


def verificar_convidado(nome, lista):
    for convidado in lista:
        if convidado.lower() == nome.lower():
            print(f"{convidado} está na lista de convidados.")
            return

    print(f"{nome} não está na lista de convidados.")


nome = input("Digite o nome do convidado: ")

verificar_convidado(nome, convidados

l = [5, 10, 20, 21, 3, 15, 1, 2, 18, 26]

n = int(input("Digite um numero:\n"))

def buscar_sequencial(l, n):

    for i in range(len(l)):
        if l[i] == n:
            return i
    else:
        return -1
        
print(buscar_sequencial(l, n))
    

