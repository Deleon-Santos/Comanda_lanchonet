import modulo_conexao as conexao

def consulta_comanda():
    # Conectando ao banco de dados
  
    try:
        conectar, cursor = conexao.conectar_db()
        print("CONSULTAR COMANDA".center(55, "-"))
        print("0 - Todas".rjust(55))
        pesquisar_numero_comanda = int(input("\nDigite o número da comanda>> "))

        if pesquisar_numero_comanda == 0:  # Consulta todas as comandas
            print("Com            Lanche          Quantidade         Preço")

            cursor.execute("""
                select id_comanda, nome_lanche, qtd_lanche, preco_lanche 
                from itens_comanda
            """)
            lista_produto = cursor.fetchall()

            for lanche in lista_produto:
                id_comanda = lanche[0]
                nome = lanche[1]
                quantidade = lanche[2]
                preco = lanche[3]
                
                print(f'{id_comanda:<15} {nome:<15} {quantidade:<17} {preco:>5.2f}')
                
        else:
            # Consulta específica para uma comanda
            cursor.execute("""
                select id_comanda, nome_lanche, qtd_lanche, preco_lanche 
                from itens_comanda 
                where id_comanda = %s
            """, (pesquisar_numero_comanda,))
            lista_produto = cursor.fetchall()

            if lista_produto:
                print("Com            Lanche          Quantidade         Preço")
                for lanche in lista_produto:
                    id_comanda = lanche[0]
                    nome = lanche[1]
                    quantidade = lanche[2]
                    preco = lanche[3]
                    
                    print(f'{id_comanda:<15} {nome:<15} {quantidade:<17} {preco:>5.2f}')
            else:
                print(f"Nenhuma comanda encontrada com o número {pesquisar_numero_comanda}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conectar.close()



