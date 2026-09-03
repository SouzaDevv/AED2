'''#Atividades

    Exercício 1: Considere a função abaixo, que recebe uma lista e imprime o primeiro elemento: 
    def imprime_primeiro(lista): 
    print(lista[0]) 
    Qual é a ordem de complexidade de tempo dessa função em termos de n (tamanho da lista)

    Resposta: A complexidade de tempo é O(1)

#######################################################################################################################################################

    Exercício 2: Analise a complexidade da função encontrar_maximo(lista) que retorna o maior valor em uma lista: 
    def encontrar_maximo(lista): 
    valor_maximo = lista[0] 
    for numero in lista: 
    if numero > valor_maximo: 
    valor_maximo = numero 
    return valor_maximo 
    A lista de entrada tem n elementos. Qual a ordem de complexidade em função de n? 

    resposta: a complexidade é O(n)

#######################################################################################################################################################

    Exercício 3: Qual a complexidade da busca binária? Considere que temos uma lista ordenada de tamanho n e 
    a função abaixo procura um elemento alvo nessa lista (retornando o índice ou -1 se não encontrar): 
    def busca_binaria(lista, alvo): 
    esquerda = 0 
    direita = len(lista) - 1 
    while esquerda <= direita: 
    meio = (esquerda + direita) // 2 
    if lista[meio] == alvo: 
    return meio 
    elif lista[meio] < alvo: 
    esquerda = meio + 1 
    else: 
    direita = meio - 1 
    return -1 
    Qual é a ordem de complexidade em função de n?

    resposta: A complexidade é de O(log n)

#######################################################################################################################################################

    Exercício 4:  Considere o seguinte código que verifica se uma lista idades contém pelo menos duas ocorrências 
    da menor idade presente na lista. Existem duas implementações diferentes para essa tarefa: 
    def existe_2_menores_v1(idades): 
    tamanho = len(idades) 
    menor = 200  # supondo idades até 200 
    # encontra a menor idade 
    for i in range(tamanho): 
    if idades[i] < menor: 
    menor = idades[i] 
    # conta ocorrências da menor idade 
    cont = 0 
    for i in range(tamanho): 
    if idades[i] == menor: 
    cont += 1 
    return cont > 1 
    def existe_2_menores_v2(idades): 
    idades.sort()  # ordena a lista 
    return idades[0] == idades[1] 
    Qual das duas funções tem menor complexidade de tempo? Justifique indicando as ordens de complexidade 
    de cada uma.

    resposta: a ordem de complexidade é de O(n log n)

#######################################################################################################################################################

    Exercício 5: A função abaixo calcula o n-ésimo número de Fibonacci de forma recursiva (definindo fib(0)=0, 
    fib(1)=1): 
    def fib(n): 
    if n < 2: 
    return n 
    else: 
    return fib(n-1) + fib(n-2) 
    Qual é a complexidade de tempo dessa implementação em termos de n? 

    resposta: A complexidade é O(2ⁿ)

#######################################################################################################################################################

    Exercício 6: Suponha que você tenha duas implementações para verificar se um número está presente em uma 
    lista. A primeira simplesmente percorre todos os elementos da lista; a segunda primeiro ordena a lista e depois 
    realiza busca binária. Qual abordagem é mais eficiente considerando a complexidade? 

    resposta: Caso seja uma busca única, a melhor opção é a de complexidade O(n), pois é mais eficiente. 
    Caso haja múltiplas buscas na mesma lista, ordenar uma vez (O(n log n)) junto de buscas binárias (O(log n) cada) é muito mais eficiente no total.

#######################################################################################################################################################




#Projeto 1


system = {"12345678900": {"nome": "João Silva", "curso": "Ciência de Dados"},
    "98765432100": {"nome": "Maria Souza", "curso": "Engenharia"},
    "11122233344": {"nome": "Pedro Santos", "curso": "Administração"},
    "55566677788": {"nome": "Ana Costa", "curso": "Direito"},
    "99988877766": {"nome": "Lucas Oliveira", "curso": "Medicina"}}


def buscar_eficiente_aluno(cpf):

    if cpf in system:
        print(system[cpf])
    else:
        print("Não encontrado")

def busca_aluno_linear(cpf):

    for i in system:
        if i == cpf:
            print(system[cpf])
            return
    else:
        print("Não encontrado")


while True:

    print("escolha uma opção\n[1] busca eficiente\n[2] busca nao eficiente\n")
    op = input("")

    if op == "1":
        cpf = input("Digite um cpf\n")
        buscar_eficiente_aluno(cpf)

    else:
        cpf = input("Digite um cpf\n")
        busca_aluno_linear(cpf)

#######################################################################################################################################################
'''
#Projeto 2

original = {
    "nome": "Anderlimson",
    "historico": ["Matemática", "Portugues"]
}
solicitacoes = []
alunos = [
    {
        "nome": "Ana",
        "historico": ["Matemática", "Português", "Ciências", "História"]
    },
    {
        "nome": "Bruno",
        "historico": ["Português", "Geografia", "Matemática"]
    },
    {
        "nome": "Carlos",
        "historico": ["Matemática", "Ciências", "Educação Física"]
    },
    {
        "nome": "Daniela",
        "historico": ["Português", "História", "Geografia", "Artes"]
    },
    {
        "nome": "Eduardo",
        "historico": ["Matemática", "Português", "Ciências"]
    },
    {
        "nome": "Fernanda",
        "historico": ["Português", "Matemática", "Artes", "História"]
    },
    {
        "nome": "Gabriel",
        "historico": ["Matemática", "Geografia", "Ciências"]
    },
    {
        "nome": "Helena",
        "historico": ["Português", "História", "Artes"]
    },
    {
        "nome": "Igor",
        "historico": ["Matemática", "Português", "Educação Física"]
    },
    {
        "nome": "Juliana",
        "historico": ["Português", "Ciências", "Geografia", "Artes"]
    },
    {
        "nome": "Lucas",
        "historico": ["Matemática", "História", "Geografia"]
    },
    {
        "nome": "Mariana",
        "historico": ["Português", "Matemática", "Ciências"]
    },
    {
        "nome": "Nathan",
        "historico": ["Matemática", "Ciências", "Educação Física"]
    },
    {
        "nome": "Olivia",
        "historico": ["Português", "História", "Geografia"]
    },
    {
        "nome": "Pedro",
        "historico": ["Matemática", "Português", "História", "Ciências"]
    },
    {
        "nome": "Rafael",
        "historico": ["Matemática", "Geografia", "Educação Física"]
    },
    {
        "nome": "Sofia",
        "historico": ["Português", "Matemática", "Artes"]
    },
    {
        "nome": "Thiago",
        "historico": ["Ciências", "História"]
    },
    {
        "nome": "Valentina",
        "historico": ["Português", "Geografia", "Artes", "Ciências"]
    },
    {
        "nome": "Vinicius",
        "historico": ["Matemática", "Português", "Geografia"]
    }
]


for aluno in alunos:
    if any(materia in aluno["historico"] for materia in original["historico"]):
        solicitacoes.append(aluno["nome"])

print(solicitacoes)