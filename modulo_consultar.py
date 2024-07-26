#funcao para consultar comandas salvas no bd
import modulo_conexao as conexao
def consulta_comanda():
    try:
        conectar, cursor = conexao.conectar_db()#abre a conexao e extrai o cursor
        print("CONSULTAR COMANDA".center(55, "-"))
        print("0 - Todas".rjust(55))
        
        pesquisar_numero_comanda = int(input("\nDigite o número da comanda>> "))
        if pesquisar_numero_comanda == 0:  # Consulta todas as comandas
            print("Com     Item         Lanche       Quantidade      Preço")

            cursor.execute("""
                SELECT id_comanda, nome_lanche, qtd_lanche, preco_lanche 
                FROM itens_comanda
            """)
            lista_produto = cursor.fetchall()
            
            if lista_produto:
                for lanche in lista_produto:
                    id_comanda = lanche[0]
                    nome = lanche[1]
                    quantidade = lanche[2]
                    preco = lanche[3]
                    
                    print(f'{id_comanda:<8} {nome:<12} {quantidade:<12} {preco:<5}', end="")
                    print(f"R$ {preco:.2f}".rjust(15))
            else:
                print('Não temos nenhum registro de comanda')
       
        else:
            cursor.execute("""
                select id_comanda, nome_lanche, qtd_lanche, preco_lanche 
                from itens_comanda 
                where id_comanda = %s
            """, (pesquisar_numero_comanda,))# Consulta específica para uma comanda pelo numero da comanda
            lista_produto = cursor.fetchall()

            if lista_produto:
                print("Com     Item         Lanche       Quantidade      Preço")
                for lanche in lista_produto:
                    id_comanda = lanche[0]
                    nome = lanche[1]
                    quantidade = lanche[2]
                    preco = lanche[3]
                    
                    print(f'{id_comanda:<8} {nome:<12} {quantidade:<12} {preco:<5}', end="")
                    print(f"R$ {preco:.2f}".rjust(15))
            else:
                print(f"Nenhuma comanda encontrada com o número {pesquisar_numero_comanda}")

    except Exception as e:
        print('Erro: {e}')
    finally:
        if cursor:
            cursor.close()
        if conectar:
            conectar.close()
        # Fechar o cursor e a conexão