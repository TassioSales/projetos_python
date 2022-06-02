import sqlite3
from sqlite3 import Error

caminho = "C:/Users/tassi//OneDrive - CESB - Centro de Educação Superior de Brasilia " \
          "LTDA/projetos/Projetos/projetos_python/banco_de_dados/banco/agenda.db "


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
            N_IDCONTATO INTERGER PRYMARY KEY AUTO_INCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
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
