venda = []
produtos = ["arroz","feijao","cereais","pizza","chocolate"]
stock = [8,4,7,10,2]

def mostrar_produtos():
    print("\n\033[33m=== PRODUTOS DISPONÍVEIS ===\033[0m")
    for i in range(len(produtos)):
        print(f"\033[36m{i+1}.\033[0m {produtos[i]} - \033[32m{stock[i]} unidades\033[0m")

while True:
    perfil = input("\nVocê é \033[32mcomprador\033[0m ou \033[34madmin\033[0m?\n> ")

    # ================= COMPRADOR =================
    if perfil == "comprador":
        print("\nDigite \033[31m'end'\033[0m para sair")

        while True:
            mostrar_produtos()
            p = input("\nQual produto queres?\n> ")

            if p == "end":
                break

            if p not in produtos:
                print("\033[31mProduto inválido!\033[0m")
                continue

            posicao = produtos.index(p)

            print(f"\033[32mStock disponível:\033[0m {stock[posicao]}")

            quant = int(input("Quantidade: "))

            if quant > stock[posicao]:
                print("\033[31mNão há stock suficiente!\033[0m")
            else:
                stock[posicao] -= quant
                venda.append((p, quant))

                print("\033[32mProduto adicionado ao carrinho!\033[0m")

                conf = input("Quer algo mais? (s/n): ")

                if conf == "n":
                    print("\n\033[35m=== COMPRA FINALIZADA ===\033[0m")
                    print("Produtos:", venda)
                    print("\033[32mObrigado pela preferência!\033[0m")
                    break

    # ================= ADMIN =================
    elif perfil == "admin":
        senha = int(input("Senha: "))

        if senha == 1234:
            print("\n\033[34m=== MODO ADMIN ===\033[0m")

            while True:
                print("""
1 - Adicionar produto
2 - Repor stock
3 - Remover produto
4 - Sair
""")
                op = int(input("> "))

                if op == 1:
                    nome = input("Nome do produto: ")

                    if nome in produtos:
                        print("\033[31mJá existe!\033[0m")
                    else:
                        qtd = int(input("Quantidade: "))
                        produtos.append(nome)
                        stock.append(qtd)

                elif op == 2:
                    nome = input("Produto: ")
                    if nome in produtos:
                        qtd = int(input("Quantidade: "))
                        stock[produtos.index(nome)] += qtd
                    else:
                        print("Não existe")

                elif op == 3:
                    nome = input("Produto: ")
                    if nome in produtos:
                        idx = produtos.index(nome)
                        produtos.pop(idx)
                        stock.pop(idx)
                        print("Removido!")
                    else:
                        print("Não encontrado")

                elif op == 4:
                    print("Saindo do admin...")
                    break

        else:
            print("\033[31mSenha errada!\033[0m")

    else:
        print("\033[31mErro: opção inválida\033[0m")