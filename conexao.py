import mysql.connector
from mysql.connector import errorcode  # Trata as exceções que pode aparecer.

class conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host='localhost',
                                                    user='root',
                                                    password='',
                                                    database='flaskdb')
            return self.db_connection
        except mysql.connector.Error as erro: #Guardando as possíveis exceções na variáveis.
            if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso o banco de dados não exista , terá tratamento.
                return 'Banco de Dados não existe!, {}'.format(erro)
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Tratamento para acesso negado ao BD.
                return 'Usuário ou senha invalidos!, {}'.format(erro)
            else:
                return erro
        else:
            self.db_connection.close()
