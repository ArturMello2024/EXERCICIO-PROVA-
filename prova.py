#  Os livros serão armazenados em uma lista, onde cada elemento é um dicionário que
# representa um livro com informações como título, autor, gênero, quantidade em estoque e
# código do livro

livros = []

# FUNÇÃO ADICIONAR LIVRO
def adicionar_livro(titulo, autor, genero, quantidade, codigo):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "quantidade": quantidade,
        "codigo": codigo
    }
    livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso.")

# FUNÇÃO BUSCAR LIVRO
def buscar_livros(codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Quantidade em Estoque: {livro['quantidade']}, Código: {livro['codigo']}")
            return
    print("Erro: Código do livro não encontrado.")

# FUNÇÃO ATUALIZAR ESTOQUE
def atualizar_estoque(codigo, nova_quantidade):
    for livro in livros:
        if livro["codigo"] == codigo:
                livro["quantidade"] = nova_quantidade
                print(f"Quantidade do livro '{livro['titulo']}' atualizada para: {nova_quantidade}.")
                return True
    print("código do livro não encontrado.")
    return False   
  
# FUNÇÃO PARA EXIBIR LIVROS
def exibir_livros():
    for livro in livros:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Quantidade em Estoque: {livro['quantidade']}, Código: {livro['codigo']},")

# FUNÇÃO PARA REMOVER LIVRO
def remover_livro(codigo):
    global livros
    for livro in livros:
        if livro["codigo"] == codigo:
            livros.remove(livro)
            print(f"Livro '{livro['titulo']}' removido do estoque com sucesso.")
            return
    print("Código do livro não encontrado.")

def menu():
    while True:
        print("MENU")
        print("1 - CADASTRAR LIVRO")
        print("2 - BUSCAR LIVRO")
        print("3 - ATUALIZAR ESTOQUE")
        print("4 - REMOVER LIVRO")
        print("5 - LISTAR TODOS OS LIVROS")
        
        opcao= input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input(" Entre com o Título do Livro: ")
            autor = input(" Entre com o Autor do Livro: ")
            genero = input("Entre com o Genero do Livro: ")
            quantidade = input("Entre com o Quantidade em estoque: ")
            codigo = input("Insira o codigo do livro: ")
            adicionar_livro(titulo, autor, genero, quantidade, codigo)
            
        elif opcao == "2":
            codigo = input("Insira o codigo do livro: ")
            buscar_livros(codigo)
            
            
        elif opcao == "3":
            codigo_livro_atualizar = input("Digite o codigo do livro: ").strip()
            nova_quantidade = input("Digite a quantidade a atualizar: ").strip()
            atualizar_estoque(codigo_livro_atualizar, nova_quantidade)
        
        elif opcao == "4":
            codigo = input(" Entre com o codigo do livro a ser removido: ")
            remover_livro(codigo)
            
        elif opcao == "5":
            exibir_livros()
        
        else:
            print("opcao inválida")
menu()