# função para remover um item da comanda
def remover(lista1,valor_total_comanda):
  try:
    numero_lanche_remover=int(input('\nDigite o numero do item>>'))
    
    for lanche in lista1:
        if lanche["N_item"] == numero_lanche_remover:# exclui a partir do codigo do item
            valor_total_comanda-=lanche["Preco"]
            print(f'N°{lanche["N_item"]:<7}    {lanche["Lanche"]:<18}  -{lanche["Quantidade"]:<9}   -R$ {lanche["Preco"]:>4.2f} ')
            lista1.remove(lanche)#exclua da lista de produtos
    print("REMOVIDO".rjust(55))
    return lista1,valor_total_comanda#retorna a valor_total_comanda atualizada
  except ValueError:
    print("Não encontrada")