# Função para salvar o pedido em uma nova comanda
import modulo_conexao as conexao
dicionario = {}

def salvar_pedido(lista_desejo,valor_total_comanda):
    
    try:
        conectar, cursor = conexao.conectar_db()
        cursor.execute("insert into comandas (valor_total) values (%s);", (valor_total_comanda,))
        conectar.commit()
        id_comanda = cursor.lastrowid  # Obtém o ID da comanda inserida

        inserir_item(id_comanda, conectar, cursor, lista_desejo)
        cursor.close()
        conectar.close()
    except ValueError:
        print("Erro ao inserir comanda: ")

# Função para inserir itens na comanda
def inserir_item(id_comanda, conectar, cursor, lista_desejo):
    for pedido in lista_desejo:
        
        lanche = pedido['Lanche']
        qtd = pedido['Quantidade']
        preco = pedido['Preco']

        try:
            cursor.execute("""
                insert into itens_comanda (id_comanda, nome_lanche, qtd_lanche, preco_lanche)
                values ( %s, %s, %s, %s);
            """, (id_comanda, lanche, qtd, preco))
            conectar.commit()
            
        
        except Exception as e:
            print(f"Erro ao inserir item: {e}")
            conectar.rollback()
