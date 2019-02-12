class Projeto(object):
    def __init__(self, nome, data_inicio, data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    
    def __str__(self):
        return self.nome

class Pessoa(object):
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return self.nome

class Atividade(object):
    def __init__(self, nome, prioridade, nomePessoa, data_nascimento, nomeProjeto, data_inicio, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.pessoa = Pessoa(nomePessoa, data_nascimento)
        self.projeto = Projeto(nomeProjeto, data_inicio, data_fim)
    
    def __str__(self):
        return self.nome

atv = Atividade("Limpar", "Elevada", "Augusto Nobrega", "1874", "Projeto limpeza", "03/02/2001", "22/02/2001")
print(atv.projeto.nome)