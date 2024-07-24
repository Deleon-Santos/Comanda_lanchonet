import modulo_cardapio as cardapio
import modulo_entrada_pedido as pedido
import modulo_conexao as conexao
#import modulo_consultar as consultar


# Função para contar as comandas
def id_comanda(cursor):
    cursor.execute("SELECT COUNT(*) FROM comandas")
    return cursor.fetchone()[0]


def consulta_comanda():
    # Conectando ao banco de dados
    conectar, cursor = conexao.conectar_db()
    
    try:
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

            for lanche in lista_produto:
                id_comanda = lanche[0]
                nome = lanche[1]
                quantidade = lanche[2]
                preco = lanche[3]
                
                print(f'{id_comanda:<8} {nome:<12} {quantidade:<12} {preco:<5}', end="")
                print(f"R$ {preco:.2f}".rjust(15))
        else:
            # Consulta específica para uma comanda
            cursor.execute("""
                SELECT id_comanda, nome_lanche, qtd_lanche, preco_lanche 
                FROM itens_comanda 
                WHERE id_comanda = %s
            """, (pesquisar_numero_comanda,))
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

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conectar.close()



# ************************** Início do programa principal *************************

dic = cardapio.cardapio()

try:
    conectar, cursor = conexao.conectar_db()
    print('Conexão ok')

    while True:
        try:
            print()
            print("MENU PRINCIPAL".center(55, "-"))
            print('1-Pedir      2-Consultar      3-Cardápio       4-Totais')
            print('S-Sair')
            menu = input('>> ').upper()

            if menu == '1':
                comanda = id_comanda(cursor) + 1
                print(f"Comanda número: {comanda}")
                pedido.entrada_pedido(cursor, comanda)

            elif menu == '2':
                consulta_comanda()

            elif menu == '3':
                print("Cardápio: ", dic)

            elif menu == '4':
                print("Totais: Implement this feature as needed")

            elif menu == 'S':
                print("Deseja Encerrar o sistema?")
                print("SIM       NÃO".center(55))
                per = input(">> ").upper()
                if per == "SIM":
                    print("ENCERRANDO O SISTEMA".center(55))
                    break
            else:
                print('OPÇÃO INVÁLIDA!')

        except Exception as e:
            print(f'Erro: {e}')

except Exception as e:
    print(f'Erro ao conectar com o banco de dados: {e}')

finally:
    if cursor:
        cursor.close()
    if conectar:
        conectar.close()
