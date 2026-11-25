from datetime import datetime
from item_venda import Item_Venda
from produto import Produto
from pagamento import Pagamento


class Venda:

    _total_vendas = 0

    def __init__(self, pagamento: Pagamento, data_venda: datetime = None):
        self._valor_total = 0.0
        self._data_venda = data_venda if data_venda else datetime.now()
        self._itens: list[Item_Venda] = []
        self._pagamento = pagamento

        Venda._total_vendas += 1

    @property
    def itens(self):
        return self._itens

    def adicionar_item(self, produto: Produto, quantidade: int):
        if produto.decrementar_estoque(quantidade):
            novo_item = Item_Venda(produto, quantidade)
            self._itens.append(novo_item)
            self._valor_total += novo_item.valor
            return True
        else:
            return False

    def remover_item(self, produto: Produto):
        for item in self._itens:
            if item.produto == produto:
                self._itens.remove(item)
                self._valor_total -= item.valor
                produto.incrementar_estoque(item.quantidade)
                return True
        return False

    def calcular_valor_total(self):
        return self._valor_total

    def finalizar_venda(self):
        return self._pagamento.calcular_valor_final(self._valor_total)

    @staticmethod
    def get_total_vendas():
        return Venda._total_vendas

    def __str__(self):
        string = "\n========== COMPROVANTE =========="
        string += f"\nVenda: {self._data_venda.strftime('%d/%m/%Y %H:%M:%S')}"
        string += "\n---------------------------------"

        for item in self._itens:
            string += (
                f"\n{item.produto.descricao} | "
                f"{item.quantidade}x | "
                f"R$ {item.produto.preco_unitario:.2f} | "
                f"Subtotal: R$ {item.valor:.2f}"
            )

        string += "\n---------------------------------"
        string += f"\nValor original: R$ {self._valor_total:.2f}"
        string += f"\nValor final: R$ {self.finalizar_venda():.2f}"
        string += "\n================================="

        return string