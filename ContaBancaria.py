from datetime import datetime
import pytz
from random import randint

class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y  %H:%M:%S')

    def __init__(self, _nome, _cpf, _agencia, _num_conta):
        self._nome = _nome
        self._cpf = _cpf
        self._saldo = 0
        self._limite = None
        self._agencia = _agencia
        self._num_conta = _num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_historico__transacoes(self):
        print("Histórico de Transações:")
        for transacao in self._transacoes:
            print(transacao)

    def consultar_saldo(self):
        print("Seu _saldo é de R${:,.2f}".format(self._saldo))
        pass

    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def __limite_conta(self):
        self._limite = 1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo -valor < self.__limite_conta():
            print("Você não tem _saldo suficiente para sacar essa quantia!")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 999999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self._cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self._limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)