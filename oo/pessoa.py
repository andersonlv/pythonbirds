class Pessoa:
    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__== '__main__':
    anderson = Pessoa(nome='Anderson')
    arthur = Pessoa(anderson, nome='Arthur')
    print(Pessoa.cumprimentar(arthur))
    print(id(arthur))
    print(arthur.cumprimentar())
    print(arthur.nome)
    print(arthur.idade)
    for filho in arthur.filhos:
        print(filho.nome)
