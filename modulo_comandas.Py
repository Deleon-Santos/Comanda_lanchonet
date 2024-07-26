#Funcao para retornar a quantidade de registros iteraveis no bd
def id_comanda(cursor):
    cursor.execute("SELECT COUNT(*) FROM comandas")
    return cursor.fetchone()[0]