from Reptil import Reptil


class Jacare(Reptil):
  
    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)