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


def incerirDados(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)
        print(ex.__class__)


while True:
    nome = input("Digite seu nome: ")
    telefone = input("Digite o Telefone: ")
    email = input('Digite seu email: ')
    vcon = ConexaoBanco(caminho)
    vsql = f"""INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
              VALUES('{nome}', '{telefone}', '{email}')"""
    incerirDados(vcon, vsql)
    opc = input("Deseja inserir mais dados [s/n] ?").lower().strip()[0]
    if opc == "s":
        continue
    elif opc == 'n':
        break
    else:
        print('Valor digitado nao coresponde a [s/n]')
        pass
