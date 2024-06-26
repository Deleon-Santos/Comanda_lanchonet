# Controle de Comandas em Lanchonete
![Comanda](comanda_img.png)

## Descrição
Este software gerencia o controle de comandas em uma lanchonete. Ele permite aos usuários fazer pedidos, consultar comandas, ver o cardápio e calcular o total de vendas do dia. As funcionalidades são implementadas em Python, utilizando listas e dicionários para armazenar os dados dos produtos e das comandas.

## Funcionalidades

### `Cardapio`
Exibe o cardápio com os produtos disponíveis e seus respectivos preços.

### `Entrada de pedidos`
Gerencia a entrada de pedidos de uma comanda específica.
- Permite adicionar itens ao pedido.
- Possibilita a remoção de itens.
- Exibe o subtotal do pedido.
- Finaliza e registra o pedido para pagamento.

### `Coletar`
Coleta a quantidade de um item específico e atualiza o valor total do pedido.

### `Remover`
Remove um item específico de um pedido e atualiza o valor total.

### `Consulta pedido`
Permite a consulta das comandas registradas.
- Exibe todas as comandas ou uma específica.

### `Totais`
Calcula e exibe o total de vendas do dia, tanto em quantidade de itens quanto em valor monetário.

## Estrutura do Código

### Variáveis Globais
- `lista_produto`: Lista que armazena todos os produtos pedidos durante o dia.
- `lista1`: Lista temporária para armazenar os itens do pedido atual.
- `com`: Contador de comandas.
- `dicionario`: Dicionário temporário para armazenar os dados de um item do pedido.

### Produtos Pré-carregados
```python
dic = [
    {"cod": "1", "lanche": "xburguer", "preco": 10.90},
    {"cod": "2", "lanche": "xbacon", "preco": 9.90},
    {"cod": "3", "lanche": "xsalada", "preco": 9.90},
    {"cod": "4", "lanche": "xtudo", "preco": 15.90},
    {"cod": "5", "lanche": "refriger", "preco": 5.90}
]
```
## Conclusão
Este software fornece uma solução completa para o gerenciamento de comandas em uma lanchonete, permitindo uma operação eficiente e organizada das vendas e pedidos.

## Desenvolvedor
Deleon Santos
- Este sitema foi desenvolvido em carater academico e sua concepção inspirou possibilitou a criação do ![App Vendas](https://github.com/Deleon-Santos/APP-vendas-V2.1.1)


