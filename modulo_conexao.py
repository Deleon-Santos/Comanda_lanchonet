import mysql.connector

# função para conectar ao bd
def conectar_db():
  try:
    conect = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="lanchonetes"
    )
    cursor = conect.cursor()
    return conect,cursor
  except Exception as e:
    print(f"Erro ao conectar ao MySQL: {e}")
    return None,None



