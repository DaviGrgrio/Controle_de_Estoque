import json


# ============================================================
# FUNÇÃO: SALVAR O ESTOQUE NO ARQUIVO JSON
# ============================================================

def salvar_estoque(estoque):
    # Abre o arquivo estoque.json no modo "w" (escrita).
    # O encoding="utf-8" permite salvar caracteres como "ã", "ç" e "é".
    with open("estoque.json", "w", encoding="utf-8") as arquivo:

        # json.dump() transforma o dicionário Python em formato JSON
        # e salva o conteúdo dentro do arquivo.
        #
        # indent=4 organiza o arquivo com espaçamento.
        # ensure_ascii=False mantém os caracteres especiais.
        json.dump(estoque, arquivo, indent=4, ensure_ascii=False)


# ============================================================
# FUNÇÃO: LISTAR PRODUTOS
# ============================================================

def listar_produtos(estoque):

    # values() retorna somente os produtos do dicionário,
    # sem retornar os IDs.
    lista_produtos = list(estoque.values())

    # Verifica se não existem produtos cadastrados.
    if not lista_produtos:
        print("\nNenhum produto cadastrado no estoque.")
        return

    print("\n" + "=" * 70)
    print("                         PRODUTOS EM ESTOQUE")
    print("=" * 70)

    # Os símbolos < e > servem para alinhar o texto.
    #
    # <30 = ocupa 30 espaços e alinha à esquerda.
    # <15 = ocupa 15 espaços e alinha à esquerda.
    # <12 = ocupa 12 espaços e alinha à esquerda.
    # >10 = ocupa 10 espaços e alinha à direita.
    print(f"{'NOME':<30} {'CATEGORIA':<15} {'QUANTIDADE':<12} {'PREÇO':>10}")

    print("-" * 70)

    # Percorre cada produto da lista.
    for produto in lista_produtos:

        # f-string permite colocar valores de variáveis
        # diretamente dentro do texto.
        print(
            f"{produto['nome']:<30} "
            f"{produto['categoria']:<15} "
            f"{produto['quantidade']:<12} "
            f"R$ {produto['preco_venda']:>7.2f}"
        )

        # Verifica se a quantidade está abaixo do estoque mínimo.
        if produto["quantidade"] < produto["estoque_minimo"]:

            print()

            # \033[91m muda a cor do texto para vermelho.
            # \033[0m retorna a cor do terminal ao padrão.
            print(
                f"    \033[91mOBSERVAÇÃO:\033[0m "
                f"{produto['nome']} está abaixo do "
                f"\033[91mestoque mínimo.\033[0m"
            )

            print(
                f"    Quantidade atual: {produto['quantidade']} | "
                f"Mínimo: {produto['estoque_minimo']}"
            )

            print()

    print("=" * 70)


# ============================================================
# FUNÇÃO: BUSCAR PRODUTO
# ============================================================

def buscar_produto(estoque, id_produto):

    # Verifica se o ID informado existe no dicionário.
    if id_produto in estoque:

        # Guarda as informações do produto em uma variável.
        produto = estoque[id_produto]

        print("\n" + "=" * 40)
        print("           PRODUTO ENCONTRADO")
        print("=" * 40)

        print(f"ID: {id_produto}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Código de barras: {produto['codigo_de_barras']}")

        print("\n--- LOCALIZAÇÃO ---")
        print(f"Corredor: {produto['corredor']}")
        print(f"Prateleira: {produto['prateleira']}")

        print("\n--- ESTOQUE ---")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Estoque mínimo: {produto['estoque_minimo']}")
        print(f"Estoque máximo: {produto['estoque_maximo']}")

        print("\n--- PREÇOS ---")

        # :.2f faz o número aparecer com duas casas decimais.
        # Exemplo: 3.5 passa a ser 3.50.
        print(f"Preço de custo: R$ {produto['preco_custo']:.2f}")
        print(f"Preço de venda: R$ {produto['preco_venda']:.2f}")

        print("\n--- FORNECIMENTO ---")
        print(f"Fornecedor: {produto['fornecedor']}")
        print(f"Data de validade: {produto['data_validade']}")

        print("\n--- ATUALIZAÇÃO ---")
        print(f"Última atualização: {produto['ultima_atualizacao']}")

        print("=" * 40)

    else:

        # \033[91m muda o texto para vermelho.
        # \033[0m volta para a cor padrão.
        print("\033[91m")
        print("=" * 40)
        print("       ⚠ PRODUTO NÃO ENCONTRADO ⚠")
        print("=" * 40)
        print(f"ID informado: {id_produto}")
        print("Verifique o ID e tente novamente.")
        print("=" * 40)
        print("\033[0m")