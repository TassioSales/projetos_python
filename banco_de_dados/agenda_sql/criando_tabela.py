import sqlite3
from sqlite3 import Error

caminho = "agenda.db"

def ConexaoBanco(caminho):
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
        print(ex.__class__)
    return con


vcon = ConexaoBanco(caminho)

######Criando TB#######

vsql = """CREATE TABLE tb_contatos(
        ID INTERGER PRYMARY KEY NOT NULL,
        CONTATO VARCHAR(30),
        TELEFONE VARCHAR(14),
        EMAIL VARCHAR(30)
      );"""


def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)
        print(ex.__class__)


criarTabela(vcon, vsql)
vcon.close()
