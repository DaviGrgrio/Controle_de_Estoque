from cadastro import cadastrar, validacao_numerica
from estoque import (buscar_produto, listar_produtos, adicionar_quantidade, retirar_quantidade, excluir_produto, carregar_estoque)

    #Carrega o estoque salvo
estoque = carregar_estoque()

while True:
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
        cadastrar(estoque)
        
    elif opcao == "2":
        listar_produtos(estoque)
        
    elif opcao == "3": 
        id_produto = input("Digite o ID do produto: ")    
        buscar_produto(estoque, id_produto)
            
    elif opcao == "4":
        id_produto = input("Digite o ID do produto: ")
        quantidade = validacao_numerica("Digite a quantidade a adicionar: ")
        adicionar_quantidade(estoque, id_produto, quantidade)
        
    elif opcao == "5":
        id_produto = input("Digite o ID do produto: ")
        quantidade = validacao_numerica("Digite a quantidade a retirar: "))
        retirar_quantidade(estoque, id_produto, quantidade)
        
    elif opcao == "6":
        id_produto = input("Digite o ID do produto: ")
        excluir_produto(estoque, id_produto)
        
    elif opcao == "0":
        print("\nSaindo do sistema...")
        break
        
    else:
        print("\nOpção invalida. Digite uma opção válida.")
        
        
        
    
