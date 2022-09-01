from distutils.log import error
from re import T
from conexao import conexao 

class model: 
    def __init__(self):
    conecx = conexao()
    conecx.conectar()

def inserir(self, nome, telefone, endereco, dataDeNascimento):

    try:
        sql = "insert into person(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}','{}',{}',{}')".format(nome, telefone, endereco, dataDeNascimento)
        self.conecx.execute(sql)
        self.conecx.commit()
        return "{} Inserido!".format(self.conecx.rowcount)
        except Exception as erro:
            return erro

def consultar(self, codigo):
    try:
        sql= "select * from person where codigo = '{}'".format(codigo)
        self.conecx.execute(sql)

        for(codigo, nome, telefone, endereco, dataDeNascimento) in self.conecx:
            msg = msg + "\nCódigo {}, Nome: {}, Telefone: {}, Endereco: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
    except Exception as erro:
        return erro

