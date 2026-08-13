#exercicio 1

frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")
print(frutas)

#exercicio 2

livros = []
livros.append("O Pequeno Príncipe")
livros.append("Dom Quixote")
livros.append("1984")

removido = livros.pop()  
print(f"Livro removido: {removido}")
print(f"Pilha restante: {livros}")

#exercicio 3

clientes = []
clientes.append("Ana")
clientes.append("Bruno")
clientes.append("Carla")

clientes.append("Daniel")  # chegada do novo cliente
saiu = clientes.pop(0)     # remove o primeiro (início da fila)
print(f"Cliente que saiu: {saiu}")
print(f"Fila restante: {clientes}")



#projeto 1
contatos = {}

while True:
    try:
        nome = input("Digite seu nome: \n")
        if nome.lower() == "sair":
            break

        email = input("Email: ")
        celular = int(input("Celular: "))
        contatos[nome] = {"email": email, "celular": celular}
        print("=" * 50)

    except ValueError:
        print("Celular inválido! Digite apenas números.\n")

print("\n--- Contatos cadastrados ---")
for nome, i in contatos.items():
    print(f"{nome} - email: {i['email']} - celular: {i['celular']}\n")

#projeto 2

tarefas = ["Comer", "andar", "trabalhar, dormir"]

while True:
    adc_tarefa = input("Digite novas tarefas: caso queira sair digite 'sair'\n")
    if adc_tarefa == "sair".lower():
        break
    tarefas.append(adc_tarefa)

print(tarefas)
