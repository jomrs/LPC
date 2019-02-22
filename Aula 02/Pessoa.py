class Evento:

    def __init__(self, nomeEvento, dataEvento, dataFim):
        self.nomeEvento = nomeEvento
        self.dataEvento = dataEvento
        self.dataFim = dataFim

    def __str__(self):
        return "Nome do Evento: " + self.nomeEvento + "\nData do Evento:" + self.dataEvento

class Pessoa:

    def __init__(self, nome, dataNasc, evento):
        self.nome = nome
        self.dataNasc = dataNasc
        self.evento = evento

    def __str__(self):
        return "Nome: " + self.nome + "\nData Nascimento: " + self.dataNasc + "\nEvento:" + self.evento

class Autor(Pessoa):
    
    def __init__(self, curriculo, cpf, nome, data_nascimento):
        self.curriculo = curriculo
        super().__init__(cpf, nome, data_nascimento)

    def __str__(self):
        return "Nome: " + self.Pessoa.nome + "\nData Nascimento: " + self.Pessoa.dataNasc + "\nEvento:" + self.Pessoa.evento + "\nCategoria Autor:" + self.categoria

class Artigo:

    def __init__(self, nomeArtigo, palavras_chave, dataArtigo):
        self.nomeArtigo = nomeArtigo
        self.dataArtigo = dataArtigo
        self.palavras_chave = palavras_chave

    def __str__(self):
        return "Nome do Artigo: " + self.nomeArtigo + "\tData Artigo: " + self.dataArtigo

class ArtigoAutor:
    def __init__(self, artigo, autor):
        self.artigo = artigo
        self.autor = autor

    def __str__(self):
        return "Artigo: " + self.artigo + "\tAutor: " + self.autor

class PessoaFisica(Pessoa):

    def __init__(self, cpf, nome, data_nascimento, evento):
        self.cpf = cpf
        super().__init__(nome, data_nascimento, evento)

    def __str__(self):
        return "Nome: " + self.Pessoa.nome + "\nData Nascimento: " + self.Pessoa.dataNasc + "\nEvento:" + self.Pessoa.evento + "\nCPF:" + self.cpf

class PessoaJuridica(Pessoa):

    def __init__(self, cnpj, nome, data_nascimento, evento):
        self.cnpj = cnpj
        super().__init__(nome, data_nascimento, evento)

    def __str__(self):
        return "Nome: " + self.Pessoa.nome + "\nData Nascimento: " + self.Pessoa.dataNasc + "\nEvento:" + self.Pessoa.evento + "\nCNPJ:" + self.cnpj

pf = PessoaFisica("11111", "thomas", "97", Evento("Xodrom", "03/02", "31/02"))
print(pf.nome)



