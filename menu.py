estoque = {}
print("\nControle de Estoque")

print("Digite 1 para cadastrar o produto")
print("Digite 2 para consultar o estoque")
print("Digite 3 para adicionar a quantidade")
print("Digite 4 para retirar a quantidade")
print("Digite 5 para sair")

opcao = input("Digite uma das opções: ")

if opcao == "1":
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
elif opcao == "2": 