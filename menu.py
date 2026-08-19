from cadastro import cadastrar
from estoque import (buscar_produto, listar_produtos, adicionar_quantidade, retirar_quantidade, excluir_produto)

estoque = {}
print("\n---------Controle de Estoque----------")
    
print("|Digite 1 para cadastrar o produto   |")
print("|Digite 2 para consultar o estoque   |")
print("|Digite 3 para buscar o produto      |")
print("|Digite 4 para adicionar a quantidade|")
print("|Digite 5 para retirar a quantidade  |")
print("|Digite 6 para excluir o produto     |")
print("|Digite 0 para sair                  |")
print("--------------------------------------")
opcao = input("\nDigite uma das opções: ")

if opcao == "1":
    cadastrar()
elif opcao == "2":
    listar_produtos()
elif opcao == "3": 
    buscar_produtos()    
elif opcao == "4":
    adicionar_produto()
elif opcao == "5":
    retirar_quantidade()
elif opcao == "6":
    excluir_produto()
elif opcao == "0":
    print("\nSaindo do sistema...")
    break
else:
    print("\nOpção invalida. Digite uma opção válida.")
    
    
    
