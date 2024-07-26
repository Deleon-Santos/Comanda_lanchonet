import modulo_cardapio as cardapio
import modulo_entrada_pedido as pedido
import modulo_conexao as conexao
import modulo_totais as totais
import modulo_comandas as com
import modulo_consultar as consultar


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
                comanda = com.id_comanda(cursor) + 1
                print(f"Comanda número: {comanda}")
                pedido.entrada_pedido( comanda)

            elif menu == '2':
                consultar.consulta_comanda()

            elif menu == '3':
                cardapio.cardapio()

            elif menu == '4':
                totais.total()

            elif menu == 'S':
                print("Deseja Encerrar o sistema?")
                print("SIM       NÃO".center(55))
                per = input(">> ").upper()
                if per == "SIM":
                    print("ENCERRANDO O SISTEMA".center(55))
                    if cursor:
                        cursor.close()
                    if conectar:
                        conectar.close()
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
