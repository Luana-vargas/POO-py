# Linguagem de Programação II
# AC03 ADS-EaD - Banco

from Cliente import Cliente
from Conta import Conta
from typing import Union, List, Dict

Number = Union[int, float]

class Banco():
    
    def __init__(self, nome: str):
        self.__nome = nome
        self.__contas = []

    def get_nome(self) -> str:
        return self.__nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        if saldo_ini < 0:
            raise ValueError("É necessário ter saldo inicial")
        numero_conta = len(self.__contas) + 1
        conta = Conta(clientes, numero_conta, saldo_ini) 
        self.__contas.append(conta) 

    def lista_contas(self) -> List['Conta']:
        return self.__contas


