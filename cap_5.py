#Atividades da lista: 

"""Exercício 1 — Objetos, encapsulamento e interface

Resposta: B.

O encapsulamento permite ocultar a representação interna do saldo e disponibilizar uma interface de alto nível para manipulação do objeto.

O atributo __saldo é privado, e o usuário da classe utiliza métodos como depositar(), sacar() e consultar_saldo() para interagir com a conta.

Exercício 2 — Herança e polimorfismo

Resposta: C — Herança e polimorfismo.

Herança: Vendedor e Gerente herdam de Funcionario.

Polimorfismo: cada classe redefine calcular_bonus() de maneira diferente, mas o método é chamado da mesma forma.

Exercício 3 — Atributo de instância x atributo de classe

Resposta: B.

Produto.contador será compartilhado e terá valor 3 após as três instanciações.

O contador pertence à classe, e não a cada objeto individualmente."""

################################################################################################################

# exercicio 4

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descricao(self):
        return f"{self.titulo} — {self.autor} ({self.paginas} páginas)"


# Programa principal
livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("O Hobbit", "J. R. R. Tolkien", 310)

print(livro1.descricao())
print(livro2.descricao())

################################################################################################################

# exercicio 5

class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("O valor do depósito deve ser positivo.")

    def consultar_saldo(self):
        return self.__saldo


# Programa principal
conta = Conta("Giovanni")

conta.depositar(500)
conta.depositar(250)

print(f"Titular: {conta.titular}")
print(f"Saldo: R$ {conta.consultar_saldo():.2f}")

################################################################################################################

# exercicio 6

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico de animal"


class Cachorro(Animal):
    def emitir_som(self):
        return "au au"


class Gato(Animal):
    def emitir_som(self):
        return "miau"


# Programa principal
animais = [
    Cachorro("Rex"),
    Gato("Mimi")
]

for animal in animais:
    print(f"{animal.nome}: {animal.emitir_som()}")

################################################################################################################

# exercicio 7 

class Veiculo:
    def __init__(self, placa, velocidade_max):
        self.__placa = placa
        self.__velocidade_max = 0
        self.__velocidade_atual = 0

        self.set_velocidade_max(velocidade_max)

    # Getter da placa
    def get_placa(self):
        return self.__placa

    # Getter da velocidade máxima
    def get_velocidade_max(self):
        return self.__velocidade_max

    # Getter da velocidade atual
    def get_velocidade_atual(self):
        return self.__velocidade_atual

    # Setter da velocidade máxima
    def set_velocidade_max(self, nova_maxima):
        if nova_maxima <= 0:
            print("A velocidade máxima deve ser positiva.")
        elif nova_maxima < self.__velocidade_atual:
            print("A nova máxima não pode ser menor que a velocidade atual.")
        else:
            self.__velocidade_max = nova_maxima

    # Método para acelerar
    def acelerar(self, incremento=10):
        if incremento > 0:
            self.__velocidade_atual += incremento

            if self.__velocidade_atual > self.__velocidade_max:
                self.__velocidade_atual = self.__velocidade_max

    # Método para frear
    def frear(self, decremento=10):
        if decremento > 0:
            self.__velocidade_atual -= decremento

            if self.__velocidade_atual < 0:
                self.__velocidade_atual = 0

    def __str__(self):
        return (
            f"Placa: {self.__placa} | "
            f"Velocidade: {self.__velocidade_atual} km/h | "
            f"Máxima: {self.__velocidade_max} km/h"
        )


# Programa principal
carro = Veiculo("ABC-1234", 100)

print(carro)

carro.acelerar(30)
print(carro)

carro.acelerar(80)
print(carro)

carro.frear(20)
print(carro)

carro.frear(100)
print(carro)

carro.set_velocidade_max(50)
print(carro)

################################################################################################################

# exercicio 8

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.05

    def __str__(self):
        return f"Funcionário: {self.nome} | Salário: R$ {self.salario:.2f}"


class Vendedor(Funcionario):
    def __init__(self, nome, salario, vendas):
        super().__init__(nome, salario)
        self.vendas = vendas

    def calcular_bonus(self):
        return (self.salario * 0.05) + (self.vendas * 0.02)


class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def calcular_bonus(self):
        return (self.salario * 0.10) + (self.equipe * 100)


# Programa principal
funcionarios = [
    Funcionario("Carlos", 3000),
    Vendedor("Ana", 2500, 10000),
    Gerente("João", 6000, 5)
]

for funcionario in funcionarios:
    print(f"Nome: {funcionario.nome}")
    print(f"Tipo: {type(funcionario).__name__}")
    print(f"Bônus: R$ {funcionario.calcular_bonus():.2f}")
    print("-" * 30)

################################################################################################################

# exercicio 9

class Produto:
    contador = 0

    def __init__(self, nome, preco):
        Produto.contador += 1

        self.__id = Produto.contador
        self.__nome = nome
        self.__preco = preco

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Setter do preço
    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("O preço deve ser maior que zero.")

    # Aplicar desconto
    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            desconto = self.__preco * (percentual / 100)
            self.__preco -= desconto
        else:
            print("O percentual deve estar entre 0 e 100.")

    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"Produto: {self.__nome} | "
            f"Preço: R$ {self.__preco:.2f}"
        )


# Programa principal
produto1 = Produto("Notebook", 3000)
produto2 = Produto("Mouse", 100)
produto3 = Produto("Teclado", 200)

print(produto1)
print(produto2)
print(produto3)

print("\nAplicando desconto no notebook...")
produto1.aplicar_desconto(10)
print(produto1)

print("\nAlterando preço do mouse...")
produto2.set_preco(120)
print(produto2)

print(f"\nTotal de produtos criados: {Produto.contador}")

################################################################################################################

# exercicio 10

class Produto:
    contador = 0

    def __init__(self, nome, preco):
        Produto.contador += 1

        self.__id = Produto.contador
        self.__nome = nome
        self.__preco = preco

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Setter do preço
    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("O preço deve ser maior que zero.")

    # Método de frete
    def calcular_frete(self):
        return 0

    def __str__(self):
        return (
            f"ID: {self.__id} | "
            f"{self.__nome} | "
            f"R$ {self.__preco:.2f}"
        )


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    def calcular_frete(self):
        return 5 + (self.peso * 2)


class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_mb):
        super().__init__(nome, preco)
        self.tamanho_mb = tamanho_mb

    def calcular_frete(self):
        return 0


class Cliente:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"Cliente: {self.__nome} | E-mail: {self.__email}"


class Pedido:
    contador = 0

    def __init__(self, cliente):
        Pedido.contador += 1

        self.__numero = Pedido.contador
        self.__cliente = cliente
        self.__produtos = []
        self.__status = "Aberto"

    def adicionar_produto(self, produto):
        if self.__status == "Fechado":
            print("Não é possível adicionar produtos a um pedido fechado.")
        else:
            self.__produtos.append(produto)
            print(f"Produto '{produto.get_nome()}' adicionado ao pedido.")

    def calcular_total(self):
        total = 0

        for produto in self.__produtos:
            total += produto.get_preco()

        return total

    def calcular_frete_total(self):
        total_frete = 0

        for produto in self.__produtos:
            total_frete += produto.calcular_frete()

        return total_frete

    def fechar_pedido(self):
        if len(self.__produtos) == 0:
            print("Não é possível fechar um pedido vazio.")
        else:
            self.__status = "Fechado"
            print("Pedido fechado com sucesso.")

    def __str__(self):
        resumo = (
            f"\n===== PEDIDO #{self.__numero} =====\n"
            f"{self.__cliente}\n"
            f"Status: {self.__status}\n"
            f"\nProdutos:\n"
        )

        for produto in self.__produtos:
            resumo += (
                f"- {produto.get_nome()} | "
                f"R$ {produto.get_preco():.2f}\n"
            )

        resumo += (
            f"\nSubtotal: R$ {self.calcular_total():.2f}\n"
            f"Frete: R$ {self.calcular_frete_total():.2f}\n"
            f"Total: R$ "
            f"{self.calcular_total() + self.calcular_frete_total():.2f}\n"
            f"=========================="
        )

        return resumo


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

cliente = Cliente(
    "Giovanni",
    "giovanni@email.com"
)

produto1 = ProdutoFisico(
    "Notebook",
    3000,
    2.5
)

produto2 = ProdutoFisico(
    "Mouse",
    100,
    0.3
)

produto3 = ProdutoDigital(
    "Curso de Python",
    200,
    1500
)

pedido = Pedido(cliente)

pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)
pedido.adicionar_produto(produto3)

print(pedido)

pedido.fechar_pedido()

produto4 = ProdutoDigital(
    "Curso de SQL",
    150,
    800
)

pedido.adicionar_produto(produto4)

print(pedido)