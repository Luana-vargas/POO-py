from Mamifero import Mamifero

class Cavalo(Mamifero):
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata) 
        self.cor_crina = cor_crina

    def galopar(self):
        return '{} galopando'.format(self.nome)  

    def relinchar(self):
       return '{} relinchando'.format(self.nome) 