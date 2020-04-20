from Reptil import Reptil

class Camaleao(Reptil):
 
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)