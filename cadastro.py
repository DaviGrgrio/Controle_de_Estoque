        # Importação para GitHub através do JSON.
import json
print(1)
estoque = []

        # Função para validar a resposta do usuário.

def validacao(msg):
    while True:
        dado = input(msg)

        if dado.strip() == "":
            print("Não pode ser nulo!")

        else:
            return dado

        # Repetição para Cadastro do Produto.

def menu_produtos():
    print("1 - Cadastrar produto")
    opcao = input("Digite uma opção: ")
    print(opcao)
    
    # Inserção de Dados.
    if opcao == "1":
        print("Você escolheu cadastrar um produto!")
        
        id = validacao(("Digite o ID do produto: ")).upper()
        nome = validacao(("Nome do produto: ")).upper()
        categoria = validacao(("Categoria do produto : ")).upper()
        codigo_de_barras = validacao(("Digite aqui o código de barras desse produto: ")).upper()
        corredor = validacao(("Digite aqui o corredor desse produto: ")).upper()
        prateleira = validacao(("Digite aqui a prateleira desse produto: ")).upper()
        quantidade = validacao(("Digite aqui a quantidade que foi reposta no estoque desse produto: ")).upper()
        estoque_minimo = validacao(("Digite aqui o estoque mínimo desse produto: ")).upper()
        estoque_maximo = validacao(("Digite aqui o estoque máximo desse produto: ")).upper()
        preco_custo = validacao(("Coloque aqui o preço de custo desse produto: R$ ")).upper()
        preco_venda = validacao(("Coloque aqui o preço de venda desse produto: R$ ")).upper()
        fornecedor = validacao("Digite aqui o fornecedor desse produto: ").upper()
        data_validade = validacao(("Digite aqui a data de validade desse produto: ")).upper()
        data = validacao("Digite aqui a data de atualização:  ").upper()

            # Dicionário de Dados.

        produto = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "codigo_de_barras": codigo_de_barras,
            "corredor": corredor,
            "prateleira": prateleira,
            "quantidade": quantidade,
            "estoque_minimo": estoque_minimo,
            "estoque_maximo": estoque_maximo,
            "preco_custo": preco_custo,
            "preco_venda": preco_venda,
            "fornecedor": fornecedor

        }

            # Exportação para o Arquivo Estoque.

        estoque.append(produto)

        arquivo = open("estoque.json", "w")
        json.dump(estoque, arquivo, indent=4)
        arquivo.close()

        print("Produto cadastrado!")

    else:
        print("Opção inválida!")
