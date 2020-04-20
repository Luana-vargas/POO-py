from Cliente import Cliente
from Banco import Banco
from typing import Union, List, Dict
Number = Union[int, float]


class Conta():
    
    def __init__(self, clientes: List[Cliente],
                 numero_conta: int,
                 saldo_inicial: Number):
        self.__clientes = clientes
        self.__numero = numero_conta
        self.__saldo = saldo_inicial
        self.__extrato = [('saldo_inicial', saldo_inicial)]

    def get_clientes(self) -> List[Cliente]:
        return self.__clientes

    def get_saldo(self) -> Number:
        return self.__saldo 

    def get_numero(self) -> int:
        return self.__numero 

    def saque(self, valor: Number) -> None:
        if valor > self.__saldo:
            raise ValueError ("Você não tem saldo suficiente para este saque")
        self.__saldo -= valor 
        self.__extrato.append(('saque', valor))

    def deposito(self, valor: Number):
        self.__saldo += valor
        self.__extrato.append(('deposito', valor))

    def extrato(self) -> List[Dict[str, Number]]:
        return self.__extrato
