import modulo_conexao as conexao

def total(cursor):
    dic=[   {"cod":"1","lanche":"xburguer","preco":10.90},
        {"cod":"2","lanche":"xbacon  ","preco":9.90},
        {"cod":"3","lanche":"xsalada ","preco":9.90},
        {"cod":"4","lanche":"xtudo   ","preco":15.90},
        {"cod":"5","lanche":"refriger","preco":5.90}]

    while True:
        try:
            print("VENDA TOTAL DO DIA".center(55))
            print('0-Voltar          1-Venda Total          2-Venda Lanche')
            
            menu = int(input('Entre com o tipo de pesquisa >> '))
            if menu !=0 and menu !=1 and menu != 2:
                print('Escolha uma opcao do menu')
                continue
            if menu == 1:
               
                cursor.execute("""
                    SELECT nome_lanche, SUM(qtd_lanche) as total_vendas, SUM(preco_lanche * qtd_lanche) as total_preco 
                    FROM itens_comanda 
                    GROUP BY nome_lanche;
                """)
                
                resultados = cursor.fetchall()
                qtd_total=0
                v_total=0
                print(f"{'Lanche':<20} {'Quantidade':<15} {'Total':>13}")
                for resultado in resultados:
                    
                    lanche, qtd, total_preco = resultado[0],resultado[1], resultado[2]
                    qtd_total+=qtd
                    v_total+=total_preco
                    print(f"{lanche:<20} {qtd:<18} {total_preco:>15.2f}")
                print()
                print(f"{'Totais  ':<21}{qtd_total:<18}{v_total:>16.2f}")
            
            elif menu == 2:
                escolha_menu = input("Selecione o código do item: ")
                try:
                    escolha_menu = int(escolha_menu)
                except ValueError:
                    print("Código inválido. Por favor, digite um número inteiro.")
                    continue

                # Verificar se o código está na lista de lanches
                lanche_encontrado = None
                for item in dic:
                    if item['cod'] == str(escolha_menu):
                        lanche_encontrado = item['lanche']
                        break

                if lanche_encontrado:
                    cursor.execute("""
                        SELECT id_comanda, nome_lanche, qtd_lanche, preco_lanche
                        FROM itens_comanda
                        WHERE nome_lanche = %s
                    """, (lanche_encontrado,))

                    resultados = cursor.fetchall()
                    if resultados:
                        print(f"{'ID Comanda':<10} {'Lanche':<12} {'Quantidade':<12} {'Preço':<8}")
                        for resultado in resultados:
                            id_comanda, nome, quantidade, preco = resultado
                            print(f"{id_comanda:<10} {nome:<12} {quantidade:<12} {preco:<8.2f}")
                    else:
                        print(f"Não foram encontradas vendas para o lanche {lanche_encontrado}.")
                else:
                    print("Lanche não encontrado.")

            elif menu == 0:
                break
            
        except Exception as e:
            print(f'{e}')
        
         


