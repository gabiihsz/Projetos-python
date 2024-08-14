# Dicionário que representa o estoque de produtos
estoque = {
    "tomate": [1000, 2.30],  # [quantidade em estoque, preço por unidade]
     "alface": [500, 0.45],  # [quantidade em estoque, preço por unidade]
     "batata": [2001, 1.20],  # [quantidade em estoque, preço por unidade]
     "feijão": [100, 1.50],  # [quantidade em estoque, preço por unidade]
}

# Inicializa a variável total que irá armazenar o custo total das vendas
total = 0

# Início do loop para registrar vendas
print("vendas:\n:")
while True:
    # Solicita o nome do produto ao usuário
    produto = input('nome do produto (fim para sair): ')

    # Verifica se o usuário deseja encerrar o programa
    if produto == 'fim':
        break

    # Verifica se o produto está disponível no estoque
    if produto in estoque:
        # Solicita a quantidade desejada do produto
        quantidade = int(input('quantidade: '))

        # Verifica se a quantidade solicitada está disponível
        if quantidade <= estoque[produto][0]:
            # Obtém o preço do produto
            preço = estoque[produto][1]
            # Calcula o custo total da venda
            custo = preço * quantidade

            # Exibe os detalhes da venda
            print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
            # Adiciona o custo da venda ao total
            total += custo
        else:
            # Mensagem de erro se a quantidade não estiver disponível
            print("Quantidade solicitada não disponível")
    else:
        # Mensagem de erro se o nome do produto for inválido
        print("Nome de produto inválido")

# Exibe o custo total das vendas
print(f" Custo total: {total:21.2f}\n")

# Exibe o estoque restante
print("Estoque:\n")
for chave, dados in estoque.items():
    print("descrição: ", chave)  # Nome do produto
    print("quantidade: ", dados[0])  # Quantidade em estoque
    print(f"preço: {dados[1]:6.2f}\n")  # Preço por unidade