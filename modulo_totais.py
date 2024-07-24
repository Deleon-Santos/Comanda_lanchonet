def total():
    print("VENDA TOTAL DO DIA".center(55))
    qtd_t=0
    som_t=0
    for l in dic:#para cada lanche
        x=l["lanche"]
        qtd=0
        somas=0
        for lanche in lista_produto:#para cada lanche em lista_produto calcuta a quantidade eo preco
            if lanche["Lanche"]==x:
                qtd+=lanche["Quantidade"]
                somas+=lanche["Preco"]
        if qtd >0:
            print(f"{x}                  {qtd}",end="")
            print(f"{somas:.2f}".rjust(28))
            qtd_t+=qtd
            som_t+=somas
    print()#escrita dos falores totais
    print(f"Total Lenches",end="")
    print(f"{qtd_t}".rjust(14))
    print(f"Soma Total ",end="")
    print(f"R$ {som_t:.2f}".rjust(44))
    print()
    print("Sair".rjust(55))
