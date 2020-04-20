# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
#
# e-mail: luana.nunes@aluno.faculdadeimpacta.com.br

from typing import Dict, List


class Pessoa:
    '''
    Classe Abstrata Pessoa - não deve ser alterada
    '''
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    Métodos que tenham exatamente a mesma implementação em todas as classes filhas
    podem ser editados nesta classe, por exemplo consulta_carga_horaria, que sempre retorna
    o valor de carga horária salvo no objeto. No entanto, todos os métodos que tenham uma
    implementação específica para dada classe, devem ser sobrescrito em tais classes.
    '''
    
    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        '''
        Construtor da classe Funcionário - lembre-se de usar o super para acessar o construtor da classe mãe
        e criar atributos que já estão definidos lá.
        '''
        super().__init__(nome, idade)
        self.horas_trabalhadas = 0
        self.salario_base_hora = 0
        self.email = email

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        return self.horas_trabalhadas * self.salario_base_hora
        

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        raise NotImplementedError

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        raise NotImplementedError

    def aumenta_salario(self) -> None:
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        aumento = (self.salario_base_hora / 100) * 5
        self.salario_base_hora += aumento

'''
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de Object, que é a classe base do Python
usada automaticamente para todos as classes que criamos).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando sempre que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
'''


class Programador(Funcionario):
    '''
    Funcionário do tipo programador:
    - salario base por hora 35.00;
    - regime de trabalho entre 20h e 40h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal e considere que o mês
      possui sempre 4.5 semanas.
    '''
    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int, ):
        super().__init__(nome, idade, email, carga_horaria_semanal)
        self.salario_base_hora = 35
        self.horas_trabalhadas = carga_horaria_semanal * 4.5

        if not (carga_horaria_semanal >= 20 and carga_horaria_semanal <= 40):
            raise ValueError
        
            


class Estagiario(Funcionario):
    '''
    Funcionário do tipo estagiário:
    - salario base por hora 15.50;
    - auxilio alimentação fixo de 250 reais por mês;
    - regime de trabalho deve estar entre 16h e 30h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal, considere que o mês
      possui sempre 4.5 semanas, e por fim adicione o auxílio alimentação.
    '''
    
    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int, ):
        super().__init__(nome, idade, email, carga_horaria_semanal)
        self.salario_base_hora = 15.50
        self.auxilio_alimentacao = 250
        self.horas_trabalhadas = carga_horaria_semanal * 4.5

        if not (carga_horaria_semanal >= 16 and carga_horaria_semanal <= 30):
            raise ValueError

    def calcula_salario(self) -> float:
        return super().calcula_salario() + self.auxilio_alimentacao

        

class Vendedor(Funcionario):
    '''
    Funcionário do tipo vendedor:
    - salario base por hora 30.00;
    - auxilio alimentação fixo de 350 reais por mês;
    - auxilio transporte fixo de 30 reais por visita realizada ao cliente;
    - regime de trabalho deve estar entre 15h e 45h semanais, caso contrário
      levanta um ValueError;
    - possui um atributo privado que guarda o número de visitas realizadas no mês,
      começando sempre em zero;
    - cálculo do sálario mensal: calcule o pagamento semanal, considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios;
    - além dos métodos de Funcionário, deve implementar os métodos:
      * realizar_visita; e
      * zerar_visitas.
    '''
    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int, ):
        super().__init__(nome, idade, email, carga_horaria_semanal)
        self.salario_base_hora = 30.00
        self.auxilio_alimentacao = 350
        self.visitas = 0
        self.auxilio_transporte = 0
        self.horas_trabalhadas = carga_horaria_semanal * 4.5


    def realizar_visita(self, n_visitas: int) -> None:
        '''
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique se n_visitas é
        um número inteiro e levante um TypeError caso contrário; Em seguida verifique
        se n_visitas é positivo e maior que zero, levantando um ValueError caso contrário.
        '''

        is_int = type (n_visitas) is int
        positivo = n_visitas > 0

        if is_int and positivo:
            self.visitas += n_visitas
            self.auxilio_transporte += n_visitas * 30
        else:
            raise ValueError


    def zerar_visitas(self) -> None:
        '''
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        '''
        self.visitas = 0

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        return super().calcula_salario() + self.auxilio_alimentacao + self.auxilio_transporte         


class Empresa:
    '''
    Classe empresa, gerencia diversos funcionários
    '''
    def __init__(self, nome: str, cnpj: int, area_atuacao: str,
                 equipe: List[Funcionario] = []):
        '''
        Construtor da classe empresa
        '''
        self.nome = nome
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
        self.equipe = equipe

    def contrata(self, novo_funcionario: Funcionario) -> None:
        '''
        Contrata um novo funcionário para a empresa (adicionando ele à lista de funcionários)
        '''
        self.equipe.append(novo_funcionario)


    def lista_fucionarios(self) -> List[Funcionario]:
        '''
        Devolve um lista com todos os funcionarios
        '''
        return self.equipe

    def folha_pagamento(self) -> float:
        '''
        Devolve o valor total gasto com o pagamento de todos os funcionários
        DICA: Itere sobre a lista de funcionários, fazendo cada objeto do tipo Funcionário
        calcular o próprio salário e acumule isso numa variável auxiliar.
        '''
        total_salarios = 0

        for funcionario in self.equipe:
            total_salarios += funcionario.calcula_salario()
    
        return total_salarios    

    def dissidio_anual(self) -> None:
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários
        DICA: idem ao método de folha de pagamento, percorra a lista de funcionários faça
        cada objeto funcionário aumentar o próprio salário base por hora.
        '''

        for funcionario in self.equipe:
            funcionario.aumenta_salario()


    def listar_visitas(self) -> Dict[str, int]:
        '''
        Retorna um dicionário com as visitas realizadas por cada vendedor;
        Como a chave do dicionário precisa ser única, deve ser usado o email do vendedor
        e o valor deve ser o número de visitas realizadas por aquele funcionário.
        DICA: percorra a lista de funcionários e use o operador 'is' para verificar se
        o funcionário é um vendedor, em caso positivo, adicione as informações pedidas
        ao dicionário, e por fim retorne esse dicionário (não precisa guardar em um atributo).
        '''
        visitas_vendedor = {}

        for funcionario in self.equipe:
            if type(funcionario) is Vendedor:
                visitas_vendedor[funcionario.email] = funcionario.visitas

        return visitas_vendedor



    def zerar_visitas_vendedores(self) -> None:
        '''
        Zera as visitas de todos os funcionário, use a dica do método listar_visitas e
        para cada vendedor, chame o método de zerar visitas do vendedor.
        '''

        for funcionario in self.equipe:
            if type(funcionario) is Vendedor:
                funcionario.zerar_visitas()
        

if __name__ == "__main__":
    luana = Vendedor("luana", 24, "luana@luana", 40)
    luana.realizar_visita(6) 
    luana.aumenta_salario()
    print("salario", luana.calcula_salario()) 
    iterative = Empresa("iterative", "32323232", "TI")
    iterative.contrata(luana)
    neo = Programador("Anderson", 25, "neo@matrix.com", 40)
    iterative.contrata(neo)
    iterative.dissidio_anual()
    print("folha: ", iterative.folha_pagamento())
    print(iterative.listar_visitas())
    iterative.zerar_visitas_vendedores()