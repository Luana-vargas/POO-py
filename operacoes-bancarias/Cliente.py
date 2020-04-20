class Cliente():
    
    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome
        self.set_telefone(telefone)
        self.__email = email 

    def get_nome(self) -> str:
        return self.__nome 

    def get_telefone(self) -> int:
        return self.__telefone

    def set_telefone(self, novo_telefone: int) -> None:
        if type (novo_telefone) is not int:  
            raise TypeError ("Você não digitou um número")
        self.__telefone = novo_telefone   

    def get_email(self) -> str:
        return self.__email 

    def set_email(self, novo_email: str) -> None:
        if novo_email.find('@') == -1:
            raise ValueError ("Digite um e-mail válido")
        self.__email = novo_email