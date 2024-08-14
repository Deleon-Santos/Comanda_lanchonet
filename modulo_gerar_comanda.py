import modulo_conexao as conexao

def comanda():
    conectar, cursor = conexao.conectar_db()  # Tentativa de conexão com o BD 

    try:
        # Seleciona o maior valor de id da tabela comandas
        cursor.execute("select max(id_comanda) from comandas")
        resultado = cursor.fetchone()[0]

        if resultado is None:
            return 0  # Ou você pode retornar None ou outro valor padrão
        else:
            return resultado

    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conectar.close()