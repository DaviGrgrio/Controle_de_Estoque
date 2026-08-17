from cadastro import cadastrar


estoque = {}
print("\n---------Controle de Estoque----------")
    
print("|Digite 1 para cadastrar o produto   |")
print("|Digite 2 para consultar o estoque   |")
print("|Digite 3 para adicionar a quantidade|")
print("|Digite 4 para retirar a quantidade  |")
print("|Digite 5 para sair                  |")
print("--------------------------------------")
opcao = input("\nDigite uma das opções: ")

if opcao == "1":
    cadastrar()
elif opcao == "2": 
    pass
    
