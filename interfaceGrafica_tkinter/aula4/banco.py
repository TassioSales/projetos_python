import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp + '/agenda.db'


def ConexaoBanco():
    conexao = None
    try:
        conexao = sqlite3.connect(nomeBanco)
        return conexao
    except Error as e:
        print(e)
    return conexao


def dql(query):
    conexao = ConexaoBanco()
    cursor = conexao.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def dml(query):
    try:
        conexao = ConexaoBanco()
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        conexao.close()
    except Error as e:
        print(e)
