import sqlite3
from sqlite3 import Error
import os

caminho = "dados/dados.db"


def ConexaoBanco(cam):
    con = None
    try:
        con = sqlite3.connect(cam)
    except Error as ex:
        print(ex)
        print(ex.__class__)
    return con


vcon = ConexaoBanco(caminho)

vsql = """CREATE TABLE agenda(
            N_IDCONTATO INTERGER PRYMARY KEY,
            NOME VARCHAR(30),
            SOBRENOME VARCHAR(30),
            DATA_EVENTO VARCHAR(10),
            HORA_EVENTO VARCHAR(10),
            TAREFA VARCHAR(30),
            DESCRICAO VARCHAR(500)
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
