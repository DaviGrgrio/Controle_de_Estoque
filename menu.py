from cadastro import cadastrar
from estoque import (buscar_produto, listar_produtos, adicionar_quantidade, retirar_quantidade, excluir produto)

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
    listar_produtos(estoque)    
elif opcao == "3":
    a

    
    
    
