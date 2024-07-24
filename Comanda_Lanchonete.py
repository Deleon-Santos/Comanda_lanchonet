import modulo_cardapio as cardapio
import modulo_entrada_pedido as pedido
import modulo_conexao as conexao
import modulo_consultar as consultar


# Função para contar as comandas
def id_comanda(cursor):
    cursor.execute("SELECT COUNT(*) FROM comandas")
    return cursor.fetchone()[0]

# ************************** Início do programa principal *************************

dic=cardapio.cardapio()

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
            comanda = id_comanda(cursor)
            comanda+=1
            print(comanda)
            pedido.entrada_pedido(cursor,comanda)

        elif menu == '2':
            consultar.consulta_pedido(cursor)

        elif menu[0] == "S":  # Encerra o programa
            print("Deseja Encerrar o sistema?")
            print("SIM       NÃO".center(55))
            per = input(">> ").upper()
            if per[0] == "S":
                print("ENCERRANDO O SISTEMA".center(55))
                break
        else:
            print('OPÇÃO INVÁLIDA!')
            continue
    except IndexError:
        print('OPÇÃO INVÁLIDA!')
        continue 
     
      