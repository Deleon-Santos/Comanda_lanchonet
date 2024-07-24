

def cardapio():
    dic=[   {"cod":"1","lanche":"xburguer","preco":10.90},
        {"cod":"2","lanche":"xbacon  ","preco":9.90},
        {"cod":"3","lanche":"xsalada ","preco":9.90},
        {"cod":"4","lanche":"xtudo   ","preco":15.90},
        {"cod":"5","lanche":"refriger","preco":5.90}]

    print("BEM-VINDO AO BOCA NERVOSA".center(55,"*"))
    print('+-------------+-----------------+---------------------+')
    print('|   CODIGO    |      PRODUTO    |        PRECO        |')
    print('+-------------+-----------------+---------------------+')
    for lanche in dic:#ler o dicionrio de cadastro e gera o cardapio co o itens atualizados
        cod, nome_lanche, preco = lanche["cod"],lanche["lanche"],lanche["preco"]
        print(f'|      {cod:<6}        {nome_lanche:<15} R$ {preco:>10.2f}    |')
    print('+-----------------------------------------------------+')



