
#                CONTROLE DE COMANDAS EM LANCHONETE
import mysql.connector


lista_produto=[]
lista1=[]
numero_de_comanda=0
dicionario={}
# with open('comanda.txt', 'r') as adic:#abrir arquivo de nome "comanda.TXT" para leitura atribuido a "adic"
#     dic = json.load(adic)#o dicionario "dic" = o aquivo JSON para leitura na variavel "adic"

dic=[   {"cod":"1","lanche":"xburguer","preco":10.90},
        {"cod":"2","lanche":"xbacon  ","preco":9.90},
        {"cod":"3","lanche":"xsalada ","preco":9.90},
        {"cod":"4","lanche":"xtudo   ","preco":15.90},
        {"cod":"5","lanche":"refriger","preco":5.90}]


#função para ver o cardapio
def cardapio():
    print("BEM-VINDO AO BOCA NERVOSA".center(55,"*"))
    print('+-------------+-----------------+---------------------+')
    print('|   CODIGO    |      PRODUTO    |        PRECO        |')
    print('+-------------+-----------------+---------------------+')
    for lanche in dic:#ler o dicionrio de cadastro e gera o cardapio co o itens atualizados
        cod, nome_lanche, preco = lanche["cod"],lanche["lanche"],lanche["preco"]
        print(f'|      {cod:<6}        {nome_lanche:<15} R$ {preco:>10.2f}    |')
    print('+-----------------------------------------------------+')

# função entra de pedidos
def entrada_pedido(numero_de_comanda):
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
            valor_total_comanda=remover(valor_total_comanda)
            continue
        #encerra o laço e rotorna o valor valor_total_comanda a ser pago
        elif lanche_escolha =="P":
            print(f"VALOR PAGO R$ {valor_total_comanda:.2f}".rjust(55))
            lista_produto.extend(lista1)#adiciona os novos itens na lista_produto
            salvar_todos_pedidos( lista1)
            lista1.clear()
            break
        #encerra o laço e anula a comando
        elif lanche_escolha=="S":
            lista1.clear()# limpa a lista1
            break
        #recebe a quantidade e processa os dados no dicionario
        else:
            numero_item+=1
            valor_total_comanda = coleta(lanche_escolha,valor_total_comanda,numero_de_comanda,numero_item)# envia e rotorna os parametros
            continue
      except ValueError:
        print('Entre com um valor numerico ')
        continue

# função para  coletar o item escolhido
def coleta(lanche_escolha,valor_total_comanda,numero_de_comanda,numero_item):
    try:
        qtd = int(input('Digite a quantidade desejada incluir>>'))
        for item in dic:# ler e atribui os valores ao dicionario
            if item["cod"]==lanche_escolha:
                dicionario = {'Pedido': numero_de_comanda,
                              'Comanda': numero_item,
                              'Lanche': item["lanche"],
                              'Quantidade': qtd,
                              'Preco': item['preco']*qtd,
                              'ValorTotal':valor_total_comanda+item['preco']*qtd }
                lista1.append(dicionario.copy())
                print(f"COMANDA N°{numero_de_comanda}".rjust(55))
                print("Item          Lanche          Quantidade          Preco")
                # ler e escre os valores na tela em forma de tabela
                for lanche in lista1:
                    pre=lanche["Preco"]
                    print(f'N°{lanche["Comanda"]:<7}    {lanche["Lanche"]:<18}   {lanche["Quantidade"]:9<}            R${pre:>6.2f}')
                print("SubTotal",end="")
                print(f"R$ {valor_total_comanda:.2f}".rjust(47))
        return valor_total_comanda#retorna o valor valor_total_comanda
    except ValueError:
        print('Entre numero_de_comanda um valor numerico ')

# função para remover um item da comanda
def remover(valor_total_comanda):
  try:
    numero_lanche_remover=int(input('\nDigite o numero do item>>'))
    for lanche in lista1:
        if lanche["Comanda"] == numero_lanche_remover:# exclui a partir do codigo do item
            valor_total_comanda-=lanche["Preco"]
            print(f'N°{lanche["Comanda"]:<7}    {lanche["Lanche"]:<18}  -{lanche["Quantidade"]:<9}   -R$ {lanche["Preco"]:>4.2f} ')
            lista1.remove(lanche)#exclua da lista de produtos
    print("REMOVIDO".rjust(55))
    return valor_total_comanda#retorna a valor_total_comanda atualizada
  except ValueError:
    print("Não encontrada")

#função para consultar a comanda
def consulta_pedido():
    try:
        print("CONSULTAR COMANDA".center(55,"-"))
        print("0-Todas".rjust(55))
        pesquisar_numero_comanda=int(input("\nDigite o numero da comanda>>"))
        if pesquisar_numero_comanda == 0:#consulta todas as comandas em lista_produto
            cont=len(lista_produto)
            if cont < 1:
                print("Com     Item         Lanche       Quantidade      Preco")
                
                return
            else:
                print("Com     Item         Lanche       Quantidade      Preco")
                for lanche in lista_produto:
                    
                    p=lanche["Preco"]
                    print(f'{lanche["Pedido"]}        {lanche["Comanda"]}          {lanche["Lanche"]}           {lanche["Quantidade"]}',end="")
                    print(f"R$ {p:.2f}".rjust(15))
                
        else:#consulta o numero informado em inpute
          print("Com     Item         Lanche       Quantidade      Preco")

          for lanche in lista_produto:
              if lanche["Pedido"] == pesquisar_numero_comanda:
                  p=lanche["Preco"]
                  print(f'{lanche["Pedido"]}        {lanche["Comanda"]}          {lanche["Lanche"]}           {lanche["Quantidade"]}',end="")
                  print(f"R$ {p:.2f}".rjust(15))
              else:
                  print(" #        #            #              #             #  ")

    except ValueError:
      print("Nao encontrada")

# função para conectar ao bd
def conectar_db():
  try:
    conect = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="lanchonete"
    )
    print("Conectado com sucesso!")
    return conect
  except Exception as e:
    print(f"Erro ao conectar ao MySQL: {e}")
    return None

# função para abri oa comanda
def salvar_todos_pedidos( lista1):
  for pedido in lista1:
    salvar_pedido( pedido)

# função para sanvar o pedido
def salvar_pedido(pedido):
  conectar=conectar_db()
  cursor = conectar.cursor()
  try:
    sql = """
      INSERT INTO pedido (id_pedido, id_lanche, nome_lanche, qtd_lanche, valor_lanche, valor_pedido)
      VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (pedido["Pedido"], pedido["Comanda"], pedido["Lanche"], pedido["Quantidade"], pedido["Preco"], pedido["ValorTotal"])
    cursor.execute(sql, valores)
    conectar.commit()
    print("Pedido salvo numero_de_comanda sucesso!")
  except Exception as e:
    print(f"Erro ao salvar pedido: {e}")
    conectar.rollback()

# função para ver totais
def total():
    print("VENDA TOTAL DO DIA".center(55))
    qtd_t=0
    som_t=0
    for l in dic:#para cada lanche
        x=l["lanche"]
        qtd=0
        somas=0
        for lanche in lista_produto:#para cada lanche em lista_produto calcuta a quantidade eo preco
            if lanche["Lanche"]==x:
                qtd+=lanche["Quantidade"]
                somas+=lanche["Preco"]
        if qtd >0:
            print(f"{x}                  {qtd}",end="")
            print(f"{somas:.2f}".rjust(28))
            qtd_t+=qtd
            som_t+=somas
    print()#escrita dos falores totais
    print(f"Total Lenches",end="")
    print(f"{qtd_t}".rjust(14))
    print(f"Soma Total ",end="")
    print(f"R$ {som_t:.2f}".rjust(44))
    print()
    print("Sair".rjust(55))


#**************************Inicio do programa principal*************************
print('*'*55)
cardapio()
while True:
    print()
    
    print("MENU PRINCIPAL".center(55,"-"))
    print('1-Pedir      2-Consultar      3-Cardapio       4-Totais')
    print('S-Sair')
    menu=input('>> ').upper()
    if menu == '1':
        numero_de_comanda+=1
        entrada_pedido(numero_de_comanda)
    elif menu == '2':
        consulta_pedido()
    elif menu == '3':
        cardapio()
    elif menu == "4":
        total()
        continue
    elif menu[0] == "S":#encerra o programa
        print("Deseja Encerrar o sistema?")
        print("SIM       NÂO".center(55))
        per=input(">>").upper()
        if per[0]== "S":
            print("ENCERRANDO O SISTEMA".center(55))
            break
    else:
        print('OPÇÃO INVALIDA!')
        continue
