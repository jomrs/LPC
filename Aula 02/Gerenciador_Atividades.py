#Com relação Muitos para Muitos || N .. N
class Projeto:
    def __init__(self, nome, data_inicio, data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    
    def __str__(self):
        return "Projeto: " + self.nome

class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return "Pessoa: " + self.nome

class Atividade:

    status = "Ativo"
    
    def __init__(self, nome, prioridade, pessoa, data_inicio, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.pessoa = pessoa
    
    def __str__(self):
        return "Atividade: " + self.nome

    def finalizar_atividade(self):
        self.status = "Finalizada"

class Endereco:
    pass

class ProjetosAtividades:
    def __init__(self, projeto, atividade):
        self.projeto = projeto
        self.atividade = atividade

    def __str__(self):
        return "Projeto: " + self.projeto.nome + "\nAtividade: " + self.atividade.nome


p = Projeto("Projeto1", "15-02-2019", "31-10-2018")
pe = Pessoa("John", "03-10-1997")
a = Atividade("atividade1", 1, pe, "17-02-2019", "19-02-2019")
ProAtividade = ProjetosAtividades(p, a)

print(ProAtividade)
