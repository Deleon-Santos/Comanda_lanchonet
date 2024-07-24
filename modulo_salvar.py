import modulo_conexao as conexao
dicionario = {}

# Função para salvar o pedido
def salvar_pedido(lista1,valor_total_comanda):
    conectar, cursor = conexao.conectar_db()
    try:
        cursor.execute("INSERT INTO comandas (valor_total) VALUES (%s);", (valor_total_comanda,))
        conectar.commit()
        id_comanda = cursor.lastrowid  # Obtém o ID da comanda inserida

        inserir_item(id_comanda, conectar, cursor, lista1)
        cursor.close()
        conectar.close()
    except ValueError:
        print("Erro ao inserir comanda: ")

# Função para inserir item na comanda
def inserir_item(id_comanda, conectar, cursor, lista1):
    for pedido in lista1:
        
        lanche = pedido['Lanche']
        qtd = pedido['Quantidade']
        preco = pedido['Preco']

        try:
            cursor.execute("""
                INSERT INTO itens_comanda (id_comanda, nome_lanche, qtd_lanche, preco_lanche)
                VALUES ( %s, %s, %s, %s);
            """, (id_comanda, lanche, qtd, preco))
            conectar.commit()
            print("Item inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir item: {e}")
            conectar.rollback()
