

import modulo_cardapio as cardapio
import modulo_entrada_pedido as pedido

import modulo_totais as totais
import modulo_gerar_comanda as com
import modulo_consultar as consultar


# ************************** Início do programa principal *************************
dic = cardapio.cardapio() #Apresentação do cardapio


    
while True:
    try:
        print()
        print("MENU PRINCIPAL".center(55, "-"))
        print('1-Pedir      2-Consultar      3-Cardápio       4-Totais')
        print('S-Sair')
        menu = input('>> ').upper()

        if menu == '1':
            comanda = com.comanda() + 1
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
            if per == "S":
                print("ENCERRANDO O SISTEMA".center(55))
                break
        else:
            print('OPÇÃO INVÁLIDA!')

    except Exception as e:
        print(f'Erro: {e}')




