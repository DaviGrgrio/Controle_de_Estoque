
        # Importação para GitHub através do JSON.
import json

from estoque import salvar_estoque

        # Função para validar a resposta do usuário.

def validacao(msg):
    while True:
        dado = input(msg)

        if dado.strip() == "":
            print("Não pode ser nulo!")

        else:
            return dado
            
def validacao_numerica(msg, tipo=int):
    while True:
        dado = validacao(msg)
        try:
            return tipo(dado)
        except ValueError:
            print("Digite um número válido!")


        # Repetição para Cadastro do Produto.

def cadastrar(estoque):
        print("Você escolheu cadastrar um produto!\n")
        
        id = validacao(("Digite o ID do produto: ")).upper()
        nome = validacao(("Nome do produto: ")).upper()
        categoria = validacao(("Categoria do produto : ")).upper()
        codigo_de_barras = validacao(("Digite aqui o código de barras desse produto: ")).upper()
        corredor = validacao(("Digite aqui o corredor desse produto: ")).upper()
        prateleira = validacao(("Digite aqui a prateleira desse produto: ")).upper()
        quantidade = validacao_numerica(("Digite aqui a quantidade que foi reposta no estoque desse produto: "))
        estoque_minimo = validacao_numerica("Digite aqui o estoque mínimo desse produto: ")
        estoque_maximo = validacao_numerica("Digite aqui o estoque máximo desse produto: ")
        preco_custo = validacao_numerica("Coloque aqui o preço de custo desse produto: R$ ",float)
        preco_venda = validacao_numerica("Coloque aqui o preço de venda desse produto: R$ ",float)
        fornecedor = validacao("Digite aqui o fornecedor desse produto: ").upper()
        data_validade = validacao(("Digite aqui a data de validade desse produto: "))
        data = validacao("Digite aqui a data de atualização:  ")

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
            "fornecedor": fornecedor,
            "data_validade": data_validade,
            "ultima_atualizacao": data
        }

            # Exportação para o Arquivo Estoque.

        estoque[id] = produto

        salvar_estoque(estoque)

        print("Produto cadastrado!")

