from Mamifero import Mamifero

class Gato(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata) 
        self.vidas = 7

    def miar(self):
        return '{} miando'.format(self.nome)  

    def morrer(self):
        if self.vidas <= 0 :
            return '{} morreu'.format(self.nome)
        self.vidas = self.vidas - 1
        return '{} tem {} vidas sobrando'.format(self.nome, self.vidas)  