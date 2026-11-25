class Pagamento:

    def calcular_valor_final(self, valor: float):
        raise NotImplementedError


class PagamentoDebito(Pagamento):

    def calcular_valor_final(self, valor: float):
        return valor


class PagamentoPix(Pagamento):

    def calcular_valor_final(self, valor: float):
        return valor * 0.95


class PagamentoDinheiro(Pagamento):

    def calcular_valor_final(self, valor: float):
        return valor * 0.97


class PagamentoCartao(Pagamento):

    def calcular_valor_final(self, valor: float):
        return valor * 1.05 q