#Pilha = LIFO -> O primeiro que entra é o ultimo que sai, e o ultimo que entra é o primeiro que sai

"""pilha = []

pilha.append("(")  # Empilha
pilha.append("[")  # Empilha

print(pilha)

pilha.pop()  # Remove o último elemento

print(pilha)

| Operação  | Conceito                                  |
# |-----------|-------------------------------------------|
# | push      | Adicionar um elemento à pilha             |
# | pop       | Remover o elemento do topo                |
# | peek      | Consultar o topo sem removê-lo            |
# | is_empty  | Verificar se a pilha está vazia            |    """

def i():
    print(50 * "=")
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print(f'PUSH {item}')

    def pop(self):
        if self.is_empty():
            print("A pilha está vazia!")
            return None

        print('POP')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("A pilha está vazia!")
            return None

        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)


S = Stack()

S.print_stack()

S.push(2)
S.push(3)
S.push(4)

S.print_stack()

S.pop()
S.pop()
S.pop()

S.print_stack()

S.push(5)
S.push(7)
S.push(8)

S.print_stack()

print(S.is_empty())

i()

def converter_bin(x):
    s = Stack()
    resultado = []
    while x > 0:
        q = x // 2
        r = x % 2
        s.push(r)
        x = q
    while not s.is_empty():
        resultado.append(s.pop())
        return resultado

print(converter_bin(10))

###########################################################################################################################################

# Questão 1
# Resposta: A
#
# Operações:
# push(5)  -> [5]
# push(10) -> [5, 10]
# pop()    -> remove 10 -> [5]
# push(7)  -> [5, 7]
# push(3)  -> [5, 7, 3]
# pop()    -> remove 3 -> [5, 7]
#
# Último pop(): 3
# Pilha final: [5, 7]


# Questão 2
# Resposta: B
#
# Operações:
# push('a') -> ['a']
# push('b') -> ['a', 'b']
# peek()    -> 'b'
# pop()     -> remove 'b' -> ['a']
# peek()    -> 'a'
#
# x = 'b'
# y = 'a'


# Questão 3
# Resposta: A
#
# I. Verdadeira: uma pilha vazia não pode realizar pop.
# II. Falsa: elementos só podem ser inseridos pelo topo.
# III. Verdadeira: o topo é o ponto de acesso da pilha.
# IV. Falsa: push é uma operação de pilha, não de fila.
#
# Corretas: I e III.


# Questão 4
# Resposta: A
#
# Operações:
# push(1) -> [1]
# push(2) -> [1, 2]
# push(3) -> [1, 2, 3]
# pop()    -> remove 3 -> [1, 2]
# push(4) -> [1, 2, 4]
# pop()    -> remove 4 -> [1, 2]
# pop()    -> remove 2 -> [1]
# pop()    -> remove 1 -> []
#
# Não ocorre nenhuma tentativa de pop() com a pilha vazia.
#
# Total: 0 vezes

# Questão 5
# Converter decimal para hexadecimal usando uma pilha

def decimal_para_hexa(n):
    if n == 0:
        return "0"

    digitos = "0123456789ABCDEF"
    pilha = []

    while n > 0:
        resto = n % 16
        pilha.append(digitos[resto])
        n = n // 16

    hexadecimal = ""

    while pilha:
        hexadecimal += pilha.pop()

    return hexadecimal


print(decimal_para_hexa(26))


# Questão 6
# Verificar se parênteses, colchetes e chaves estão balanceados

def balanceia_colchetes(expressao):
    pilha = []

    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for caractere in expressao:
        if caractere in "([{":
            pilha.append(caractere)

        elif caractere in ")]}":
            if not pilha:
                return False

            if pilha.pop() != pares[caractere]:
                return False

    return len(pilha) == 0


print(balanceia_colchetes("({[]})"))
print(balanceia_colchetes("({[}])"))


#PROJETO 1


historico = []


def aplicar_filtro(dados, filtro):
    historico.append(dados.copy())

    return [item for item in dados if filtro(item)]


def desfazer(dados):
    if not historico:
        return dados

    return historico.pop()


dados = [10, 20, 30, 40, 50]

print("Dados iniciais:", dados)

dados = aplicar_filtro(dados, lambda x: x >= 20)
print("Filtro 1:", dados)

dados = aplicar_filtro(dados, lambda x: x <= 40)
print("Filtro 2:", dados)

dados = desfazer(dados)
print("Desfazer:", dados)

dados = desfazer(dados)
print("Desfazer:", dados)



#PROJETO 2

def calcular(expressao):
    numeros = []
    operadores = []

    precedencia = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    def aplicar_operacao():
        operador = operadores.pop()

        b = numeros.pop()
        a = numeros.pop()

        if operador == "+":
            numeros.append(a + b)

        elif operador == "-":
            numeros.append(a - b)

        elif operador == "*":
            numeros.append(a * b)

        elif operador == "/":
            numeros.append(a / b)

    i = 0

    while i < len(expressao):
        caractere = expressao[i]

        if caractere == " ":
            i += 1
            continue

        if caractere.isdigit():
            numero = ""

            while i < len(expressao) and expressao[i].isdigit():
                numero += expressao[i]
                i += 1

            numeros.append(float(numero))
            continue

        if caractere == "(":
            operadores.append(caractere)

        elif caractere == ")":
            while operadores[-1] != "(":
                aplicar_operacao()

            operadores.pop()

        elif caractere in "+-*/":
            while (
                operadores
                and operadores[-1] != "("
                and precedencia[operadores[-1]] >= precedencia[caractere]
            ):
                aplicar_operacao()

            operadores.append(caractere)

        i += 1

    while operadores:
        aplicar_operacao()

    return numeros[0]


print(calcular("3 + 4 * (2 - 1)"))
print(calcular("10 + 5 * 2"))
print(calcular("(10 + 5) * 2"))
print(calcular("20 / 4 + 3"))