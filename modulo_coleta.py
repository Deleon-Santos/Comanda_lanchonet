lista1=[]
dic=[   {"cod":"1","lanche":"xburguer","preco":10.90},
        {"cod":"2","lanche":"xbacon  ","preco":9.90},
        {"cod":"3","lanche":"xsalada ","preco":9.90},
        {"cod":"4","lanche":"xtudo   ","preco":15.90},
        {"cod":"5","lanche":"refriger","preco":5.90}]

# função para  coletar o item escolhido
def coleta( lanche_escolha,valor_total_comanda,comanda,numero_item):
    
    try:
        qtd = int(input('Digite a quantidade desejada incluir>>'))
        if qtd >10:
           print('Quantidade sera aceita apenas por encomenda')
        
        for item in dic:# ler e atribui os valores ao dicionario
            if item["cod"]==lanche_escolha:
                valor_total_comanda+=item['preco']*qtd
                dicionario = {'N_comanda': comanda,
                              'N_item': numero_item,
                              'Lanche': item["lanche"],
                              'Quantidade': qtd,
                              'Preco': item['preco']*qtd,
                              'ValorTotal':valor_total_comanda }
                lista1.append(dicionario.copy())
                print(f"COMANDA N°{comanda}".rjust(55))
                print("Item          Lanche          Quantidade          Preco")
                
                # ler e escre os valores na tela em forma de tabela
                for lanche in lista1:
                    pre=lanche["Preco"]
                    print(f'N°{lanche["N_item"]:<7}    {lanche["Lanche"]:<18}   {lanche["Quantidade"]:9<}            R${pre:>6.2f}')
                print("SubTotal",end="")
                print(f"R$ {valor_total_comanda:.2f}".rjust(47))
                return valor_total_comanda,lista1
            
        return valor_total_comanda#retorna o valor valor_total_comanda
    except ValueError:
        print('Entre numero_de_comanda um valor numerico ')
