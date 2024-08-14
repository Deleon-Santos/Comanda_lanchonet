#Funcao para inserir, cancelar ou pagar um pedido
import modulo_remover as remove
import modulo_coleta as coleta
import modulo_salvar as salva

lista_produto=[]
lista_desejo=[]

def entrada_pedido(comanda):
    valor_total_comanda, numero_item = 0, 0
    print("NOVO PEDIDO".center(55,"-"))
    
    while True:
        try:
            print("S-SAIR                C-CANCELAR                P-PAGAR\n")
            
            lanche_escolha = input('Digite o código do lanche que deseja>>').upper()
            if lanche_escolha[0] not in "12345SPC":
                print('Escolha uma opção dentro do cardapio')
                continue
            elif lanche_escolha[0]=="C":
                if lista_desejo:           
                    lista_desejo,valor_total_comanda=remove.remover(lista_desejo,valor_total_comanda)
                else:
                    print("Não há itens de desejo")
                continue

            elif lanche_escolha =="P":
                print(f"VALOR PAGO R$ {valor_total_comanda:.2f}".rjust(55))
                lista_produto.extend(lista_desejo)#adiciona os novos itens na lista_produto
                
                salva.salvar_pedido(lista_desejo,valor_total_comanda)
                lista_desejo.clear()
                break
            
            elif lanche_escolha=="S":
                return comanda-1
            #recebe a quantidade e processa os dados no dicionario
            else:
                numero_item+=1
                
                valor_total_comanda, lista_desejo = coleta.coleta(lanche_escolha,valor_total_comanda,comanda,numero_item)
                continue

        except ValueError:
            print('Entre com um valor numerico ')
            continue
        except :
            print("Item não localizadoss")
            continue