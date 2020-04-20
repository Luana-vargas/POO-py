class Reptil:
   
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)