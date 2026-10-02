"""#Filas: FIFO

class Queue:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return not self.itens == []

    def enqueue(self, item):
        self.itens.insert(0, item) # O insert recebe 2 parametros (_ _) o primeiro parametro é a posição, o segundo seria oque será colocado no indice; 
                                   #quando usamos.append, ele coloaria no começo da fila
        print(f"ENQUEUE {item}")

    def dequeue(self):
        print("DEQUEUE")
        return self.itens.pop()

    def size(self):
        return len(self.itens)

    def print_queue(self):
        print(self.itens)
    
fila = Queue()

print(fila.is_empty())

fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C")

fila.print_queue()

print(fila.dequeue())

print(fila.size())"""

############################################################################################################################################################

#insert(0) + pop(1) -> O(n) O(1)
#append(1) + pop(0) > O(1)  O(n)

############################################################################################################################################################

#BATATA QUENTE
class Node:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


class BatataQuente:
    def __init__(self):
        self.front = None
        self.rear = None
        self.atual = None

    def adicionar_crianca(self, nome):
        nova = Node(nome)

        if self.front is None:
            self.front = nova
            self.rear = nova
            self.atual = nova
            nova.proximo = nova

        else:
            nova.proximo = self.front
            self.rear.proximo = nova
            self.rear = nova

    def passar_batata(self):
        self.atual = self.atual.proximo

    def remover_atual(self):
        if self.front == self.rear:
            nome = self.atual.nome

            self.front = None
            self.rear = None
            self.atual = None

            return nome

        anterior = self.front

        while anterior.proximo != self.atual:
            anterior = anterior.proximo

        nome = self.atual.nome

        anterior.proximo = self.atual.proximo

        if self.atual == self.front:
            self.front = self.atual.proximo

        if self.atual == self.rear:
            self.rear = anterior

        self.atual = self.atual.proximo

        self.rear.proximo = self.front

        return nome

    def jogar(self, quantidade_passes):
        while self.front != self.rear:

            atual = self.front

            while True:
                print(atual.nome, end=" → ")
                atual = atual.proximo

                if atual == self.front:
                    break

            print("(volta)")

            for i in range(quantidade_passes):
                self.passar_batata()
                print(f"Passou a batata: {self.atual.nome}")

            eliminado = self.remover_atual()

            print(f"{eliminado} foi eliminado!")

        print(f"\nVencedor: {self.front.nome}")


batata = BatataQuente()

batata.adicionar_crianca("João")
batata.adicionar_crianca("Maria")
batata.adicionar_crianca("Carlos")
batata.adicionar_crianca("Ana")
batata.adicionar_crianca("Pedro")

batata.jogar(3)
