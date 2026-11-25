from produto import Produto
from venda import Venda
from pagamento import (
    PagamentoDebito,
    PagamentoPix,
    PagamentoDinheiro,
    PagamentoCartao
)


produto1 = Produto("Mouse", 100.00, 20)
produto2 = Produto("Teclado", 150.00, 20)
produto3 = Produto("Monitor", 1000.00, 10)


# Venda 1 - Pix
venda1 = Venda(PagamentoPix())
venda1.adicionar_item(produto1, 2)

print(venda1)


# Venda 2 - Débito
venda2 = Venda(PagamentoDebito())
venda2.adicionar_item(produto2, 1)

print(venda2)


# Venda 3 - Cartão
venda3 = Venda(PagamentoCartao())
venda3.adicionar_item(produto3, 1)

print(venda3)


# Venda 4 - Dinheiro
venda4 = Venda(PagamentoDinheiro())
venda4.adicionar_item(produto2, 2)

print(venda4)


# Quantidade total de vendas
print("\nQuantidade de vendas criadas:", Venda.get_total_vendas())