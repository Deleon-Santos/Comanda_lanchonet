import modulo_remover as remove
import modulo_coleta as coleta
import modulo_salvar as salva

lista_produto=[]

def entrada_pedido(comanda):
    valor_total_comanda, numero_item = 0, 0
    print("NOVO PEDIDO".center(55,"-"))
    while True:
      try:
        print("S-SAIR                C-CANCELAR                P-PAGAR\n")
        lanche_escolha = input('Digite o código do lanche que deseja>>').upper()
        #retorna o laço quando as opções sao invalidas
        if lanche_escolha[0] not in "12345SPC":
            print('Escolha uma opção dentro do cardapio')
        #cancela o item e retorna a valor_total_comanda atualizada
        
        elif lanche_escolha[0]=="C":
            
            lista1,valor_total_comanda=remove.remover(lista1,valor_total_comanda)
            continue
            #encerra o laço e rotorna o valor valor_total_comanda a ser pago

        elif lanche_escolha =="P":
            print(f"VALOR PAGO R$ {valor_total_comanda:.2f}".rjust(55))
            
            lista_produto.extend(lista1)#adiciona os novos itens na lista_produto
            salva.salvar_pedido(lista1,valor_total_comanda)
            
            lista1.clear()
            break
        #encerra o laço e anula a comando
        elif lanche_escolha=="S":
            lista1.clear()# limpa a lista1
            break
        #recebe a quantidade e processa os dados no dicionario
        else:
            numero_item+=1
            
            valor_total_comanda, lista1 = coleta.coleta(lanche_escolha,valor_total_comanda,comanda,numero_item)# envia e rotorna os parametros
            
            continue
      except ValueError:
        print('Entre com um valor numerico ')
        continue