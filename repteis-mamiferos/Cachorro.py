from Mamifero import Mamifero

class Cachorro(Mamifero):
   
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata) 
        self.raca = raca

    def latir(self):
        return '{} latindo'.format(self.nome)  

    def rosnar(self):
       return '{} rosnando'.format(self.nome) 