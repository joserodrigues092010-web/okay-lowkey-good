venda = []
produtos = ["arroz","feijao","cereais","pizza","chocolate"]
stock = [8,4,7,10,2]
print(produtos)
while True:
    perfil = input("Você é um \033[32mcomprador\033[0m ou um \033[34madmin\033[0m?\n ")
    if perfil == "comprador":
        print ("se quiser parar digite (end)")
        while True:
            print (produtos)
            p = input("qual produto tu queres?\n")
            if p == "end":
                break
            elif p not in produtos:
                print ("produto invalido insira outro")
            else:
                posicao = produtos.index(p)
            print("há",stock[posicao],p,"no stock")
            quant = int(input("qual é a quantidade do produto?\n "))
            if quant > stock[posicao]:
                print ("não ha no estoque")
            else:
                venda.append((p,quant))
                conf = input("quer algo a mais? (s/n)\n")
                if conf == "s":
                    stock[posicao] -= quant
                elif conf !="n" and conf !="s":
                    print("erro de sintaxe")
                    break
                else:
                    print("produtos adquiridos: \n",venda,)
                    print("obrigado pela preferencia")
                    sair = True
                    break
    elif perfil == "admin":
        senha = int(input("digite a senha: \n"))
        if senha == 1234:
            print("Item=\n ",produtos)
            print("Quantidade=\n ",stock)
            while True:
                pergunta = int(input("deseja adicionar algo ao estoque(1), recolocar(2) , tirar(3) ou confirmar as alterações (4)?\n"))
                if pergunta == 1:
                    qual= input("qual é o nome do produto que desejas adicionar? ")
                    if qual in produtos:
                        print("produto ja esta no estoque")
                    else:
                        qual1= int(input("e qual é a quantidade? "))
                        produtos.append(qual)
                        stock.append(qual1)
                        print ((produtos,stock))
                elif pergunta == 2:
                    qual2= input("a qual produto desejas recolocar?")
                    qual3= int(input("insira a quantidade: "))
                    pos = produtos.index(qual2)
                    stock[pos] += qual3
                elif pergunta == 3:
                    qual4= input("qual produto desejas tirar?")
                    if qual4 in produtos:
                        qual5= int(input("qual é a quantidade? digite o caractere zero ´0` se quiser retirar do base de dados"))
                        if qual5== 0:
                            pos1 = produtos.index(qual4)
                            produtos.remove(pos1)
                            stock.remove(pos1)
                            print("produto removido")
                        elif qual5 >0:
                            pos1 = produtos.index(qual4)
                            stock[pos1] -= qual5
                            print("foi removido",qual5,qual4)
                        else:
                            print("Erro")
                    else:
                        print("produto não encontrado")
                elif pergunta == 4:
                    print("mudanças salvas")
                    break
                else:
                    print("ERROR. volte a digitar")
        else:
            print("acho que tu errou")
    else:
        print ("erro")