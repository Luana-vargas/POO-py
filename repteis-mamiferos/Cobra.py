from Reptil import Reptil


class Cobra(Reptil):
    
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return '{} rastejando'.format(self.nome)

    def trocar_pele(self):
        return '{} trocando de pele'.format(self.nome)
