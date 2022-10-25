from mailbox import NotEmptyError


class Pessoa:
    def __init__(self, nome=None, idade = None):
        self.nome = nome
        self.idade = idade
        
    #cria uma classe estatica    
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
        # print(cls)
        
    @staticmethod
    def e_dimaior(idade):
        return idade > 17
        
        
        

p = Pessoa.criar_data_nascimento(2000, 12, 11, "Junior")
print(p.nome, p.idade)


print(Pessoa.e_dimaior(18))
print(Pessoa.e_dimaior(10))