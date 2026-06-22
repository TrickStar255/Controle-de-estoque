# Projeto controle de estoque:

estoque = {}    # Um lugar para guardar os produtos.

while True: # Loop infinito para o menu.
    print ("=== CONTROLE DE ESTOQUE ===\n") # Título do programa
    print("1 - Cadastrar Produto")     # 1 - Cadastrar produto
    print("2 - Consultar Estoque")   # 2 - Consultar estoque
    print("3 - Entrada de Produto")  # 3 - Entrada de produto
    print("4 - Saída de Produto")  # 4 - Saída de produto
    print("5 - Sair\n")   # 5 - Sair

    opcao = input("Escolha uma opção: ") # Perguntar a opção para o usuário


    if opcao == "1": # Cadastrar produto
        nome = input("Digite o nome do produto: ") # Perguntar o nome do produto
        quantidade = int(input("Quantidade produto: ")) # Perguntar a quantidade do produto
        estoque[nome] = quantidade # Guardar o produto no estoque, associando o nome à quantidade.
        print("\nCadastrado com sucesso!\n") # Informar que o produto foi cadastrado com sucesso.
            
    elif opcao == "2": # Consultar estoque
        if estoque:
            print("\nEstoque atual:\n") # Informar o estoque atual
            
            for nome, quantidade in estoque.items(): # Para cada produto no estoque, mostrar o nome e qtd
                print(f"Produto: {nome} | Quantidade: {quantidade}\n") # Mostrar o nome e a quantidade do produto
        else:
            print("\nNenhum produto cadastrado no estoque,.\n") # Informar que não há produtos cadastrados no estoque.

    elif opcao == "3": # Entrada de produto
        nome = input("Digite Produto: ")
        quantidade = int(input("Quantidade: "))

        if nome in estoque: # Se o nome esta na lista eu devo.
            estoque[nome] += quantidade # Somo a quantidade do produto digitado se estiver no estoque.
            print(f"\nEntrou {quantidade} unidades o produto {nome} no estoque.\n") # Informar que o produto entrou no estoque.
        else: # Se o nome não estiver na lista eu devo.
            print(f"\nProduto {nome} não encontrado no estoque. Cadastre o produto primeiro.\n")    

    elif opcao == "4": # Saída de produto
        nome = input("Digite Produto: ") # Perguntar o nome do produto
        quantidade = int(input("Quantidade: ")) # Perguntar a quantidade do produto

        if nome in estoque:
            estoque[nome] -= quantidade # Subtrair a quantidade do produto digitado se estiver no estoque.
            print(f"\nSaíram {quantidade} unidades do produto {nome} do estoque.\n") # Informar que o produto saiu do estoque.
        else:
            print(f"\nProduto {nome} não encontrado no estoque. Cadastre o produto primeiro.\n") # Informar que o produto não foi encontrado no estoque.

    elif opcao == "5": # Sair
        print("Saindo do programa...")
        break
    else: # Opção inválidade, vi que quando estava escrevendo qualquer coisa que não fosse 1,2,3,4 ou 5 o programa encerrava tudo, então coloquei essa opção para informar o usuário que a opção é inválida, e o programa continua rodando.
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")