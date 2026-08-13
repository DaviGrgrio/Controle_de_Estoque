import json

estoque = {
    "101": {
        "nome": "Parafuso Sextavado M8",
        "categoria": "Ferragens",
        "codigo_de_barras": "7891234567890",
        "corredor": "A",
        "prateleira": 2,
        "quantidade": 150,
        "estoque_minimo": 50,
        "estoque_maximo": 500,
        "preco_custo": 0.45,
        "preco_venda": 1.2,
        "fornecedor": "Metalurgica Silva",
        "data_validade": None,
        "ultima_atualizacao": "2026-08-01 14:30"
    },

    "102": {
        "nome": "Detergente Neutro 500ml",
        "categoria": "Limpeza",
        "codigo_de_barras": "7890987654321",
        "corredor": "B",
        "prateleira": 1,
        "quantidade": 12,
        "estoque_minimo": 20,
        "estoque_maximo": 100,
        "preco_custo": 1.8,
        "preco_venda": 3.5,
        "fornecedor": "Quimica Clean",
        "data_validade": "2027-12-31",
        "ultima_atualizacao": "2026-08-05 09:15"
    },

    "103": {
        "nome": "Lâmpada LED 9W 6500K",
        "categoria": "Eletrônicos",
        "codigo_de_barras": "7895554443332",
        "corredor": "C",
        "prateleira": 4,
        "quantidade": 45,
        "estoque_minimo": 15,
        "estoque_maximo": 150,
        "preco_custo": 4.5,
        "preco_venda": 9.9,
        "fornecedor": "Luz & Cia",
        "data_validade": None,
        "ultima_atualizacao": "2026-08-06 10:00"
    }
}

json.dump(estoque, open("estoque.json", "w"))
lista_produtos = list(estoque.values())

print("\n" + "=" * 40)
print("           PRODUTO EM ESTOQUE")
print("=" * 40)

print(f"ID: {103}")
print(f"Nome: {estoque['102']['nome']}")
print(f"Categoria: {estoque['102']['categoria']}")
print(f"Código de barras: {estoque['102']['codigo_de_barras']}")

print("\n--- LOCALIZAÇÃO ---")
print(f"Corredor: {estoque['102']['corredor']}")
print(f"Prateleira: {estoque['102']['prateleira']}")

print("\n--- ESTOQUE ---")
print(f"Quantidade: {estoque['102']['quantidade']}")
print(f"Estoque mínimo: {estoque['102']['estoque_minimo']}")
print(f"Estoque máximo: {estoque['102']['estoque_maximo']}")

print("\n--- PREÇOS ---")
print(f"Preço de custo: R$ {estoque['102']['preco_custo']:.2f}")
print(f"Preço de venda: R$ {estoque['102']['preco_venda']:.2f}")

print("\n--- FORNECIMENTO ---")
print(f"Fornecedor: {estoque['102']['fornecedor']}")
print(f"Data de validade: {estoque['102']['data_validade']}")

print("\n--- ATUALIZAÇÃO ---")
print(f"Última atualização: {estoque['102']['ultima_atualizacao']}")

print("=" * 40)

def listar_produtos(lista_produtos):
    if not lista_produtos:
        print("\nNenhum produto cadastrado no estoque.")
        return

    print("\n" + "=" * 70)
    print("                         PRODUTOS EM ESTOQUE")
    print("=" * 70)

    print(f"{'NOME':<30} {'CATEGORIA':<15} {'QUANTIDADE':<12} {'PREÇO':>10}")
    print("-" * 70)

    for produto in lista_produtos:
        print(
            f"{produto['nome']:<30} "
            f"{produto['categoria']:<15} "
            f"{produto['quantidade']:<12} "
            f"R$ {produto['preco_venda']:>7.2f}"
        )

        if produto["quantidade"] < produto["estoque_minimo"]:
            print()
            print(
                f"    \033[91mOBSERVAÇÃO:\033[0m {produto['nome']} está abaixo do "
                f"\033[91mestoque mínimo.\033[0m\n"
                f"    Quantidade atual: {produto['quantidade']} | "
                f"Mínimo: {produto['estoque_minimo']}"
            )
            print()

    print("=" * 70)


listar_produtos(lista_produtos)