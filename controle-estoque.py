# Projeto controle de estoque:
import json

def salvar_estoque():
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return {}
    
def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido.")

def ler_nome(msg):
    return input(msg).strip().lower()


def cadastrar_produto():
    nome = ler_nome("Digite o nome do produto: ")

    if nome in estoque:
            print(f"\n Este produto já está cadastrado!\n")
    else:
        quantidade = ler_inteiro("Quantidade produto: ")
        estoque[nome] = quantidade 
        salvar_estoque()
        print("\nCadastrado com sucesso!\n")

def consultar_estoque():
    if estoque:
        print("\nEstoque atual:\n")
            
        for nome, quantidade in estoque.items():
            if quantidade >= 0:
                print(f"Produto: {nome} | Quantidade: {quantidade}\n")
            else:
                print(f"Produto: {nome} | PENDENTE: {quantidade} (comprar {abs(quantidade)})")
    else:
        print("\nNenhum produto cadastrado no estoque,.\n")

def entrada_de_produto():
    nome = ler_nome("Digite o nome do produto: ")
    quantidade = ler_inteiro("Quantidade: ")

    if nome in estoque:
        estoque[nome] += quantidade
        salvar_estoque()
        print(f"\nEntrou {quantidade} unidades do produto {nome} no estoque.\n")
    else:
        print(f"\nProduto {nome} não encontrado no estoque. Cadastre o produto primeiro.\n")

def excluir_produto():
    nome = ler_nome("Digite o nome do produto a ser excluído: ")

    if nome in estoque:
        resposta = input(f"\nProduo {nome} foi encontrado. Deseja excluir? (s/n): ")

        if resposta.strip().lower() == "s":
            del estoque[nome]
            salvar_estoque()
            print(f"\nProduto {nome} excluído do estoque.\n")
        else:
            print("\nExclusão cancelada!\n")
            
    else: 
        print(f"\nProduto {nome} não encontrado no estoque.\n")

def saida_de_produto():
    nome = ler_nome("Digite o nome do produto: ")
    quantidade = ler_inteiro("Quantidade: ")

    if nome in estoque:
        estoque[nome] -= quantidade

        salvar_estoque()
        print(f"\nSaíram {quantidade} unidades do produto {nome} do estoque.\n")
   
    else:
        print(f"\nProduto {nome} não encontrado no estoque. Cadastre o produto primeiro.\n")


estoque = carregar_estoque()

while True:
    print ("=== CONTROLE DE ESTOQUE ===\n")
    print("1 - Cadastrar Produto")
    print("2 - Consultar Estoque")
    print("3 - Entrada de Produto")
    print("4 - Saída de Produto")
    print("5 - Excluir Produto")
    print("6 - Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()   
    elif opcao == "2":
        consultar_estoque()
    elif opcao == "3":
        entrada_de_produto()   
    elif opcao == "4":
        saida_de_produto()
    elif opcao == "5":
        excluir_produto()
    elif opcao == "6": # Sair
        print("Saindo do programa...")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")