class Evento:

    def __init__(self, nomeEvento, dataEvento):
        self.nomeEvento = nomeEvento
        self.dataEvento = dataEvento

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
    
    def __init__(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return "Nome: " + self.Pessoa.nome + "\nData Nascimento: " + self.Pessoa.dataNasc + "\nEvento:" + self.Pessoa.evento + "\nCategoria Autor:" + self.categoria

class Artigo:

    def __init__(self, nomeArtigo, dataArtigo):
        self.nomeArtigo = nomeArtigo
        self.dataArtigo = dataArtigo

    def __str__(self):
        return "Nome do Artigo: " + self.nomeArtigo + "\tData Artigo: " + self.dataArtigo

class ArtigoAutor:
    def __init__(self, artigo, autor):
        self.artigo = artigo
        self.autor = autor

    def __str__(self):
        return "Artigo: " + 

class PessoaFisica(Pessoa):

    def __init__(self, cpf):
        self.cpf = cpf

    def __str__(self):
        return "Nome: " + self.Pessoa.nome + "\nData Nascimento: " + self.Pessoa.dataNasc + "\nEvento:" + self.Pessoa.evento + "\nCPF:" + self.cpf

class PessoaJuridica(Pessoa):

    def __init__(self, cnpj):
        self.cnpj = cnpj

    def __str__(self):
        return "Nome: " + self.Pessoa.nome + "\nData Nascimento: " + self.Pessoa.dataNasc + "\nEvento:" + self.Pessoa.evento + "\mCNPJ:" + self.cnpj


