import os
import sqlite3
from sqlite3 import Error


##Conexão com o banco de dados
def ConexaoBanco():
    try:
        conexao = sqlite3.connect('agenda.db')
        return conexao
    except Error as e:
        print(e)
        return None


vcon = ConexaoBanco()  # Cria a conexão com o banco de dados


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)
        return None
    finally:
        print("Executado com sucesso!")
        conexao.close()


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


def menuPrincipal():
    os.system("cls")
    print("""
    1 - Inserir novo contato
    2 - Deletar Registro
    3 - Alterar contato
    4 - Consultar Registro (ID)
    5 - Consulta contato (Nome)
    6 - Sair""")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


def inserirContato():
    os.system("cls")
    vnome = input("Digite o nome do contato: ")
    vtelefone = input("Digite o telefone do contato: ")
    vemail = input("Digite o email do contato: ")
    vsql = "INSERT INTO tb_contatos (NOME, TELEFONE, EMAIL) VALUES ('" + vnome + "', '" + vtelefone + "', '" + vemail + "') "
    query(vcon, vsql)


def deletarContato():
    os.system("cls")
    vid = input("Digite o ID do contato que deseja deletar: ")
    vsql = "DELETE FROM tb_contatos WHERE ID = " + vid
    query(vcon, vsql)


def alterarContato():
    vid = input("Digite o ID do contato que deseja alterar: ")
    resp =consultar(vcon, "SELECT * FROM tb_contatos WHERE ID = " + vid)
    rnome = resp[0][1]
    rtelefone = resp[0][2]
    remail = resp[0][3]
    vnome = input("Digite o nome do contato: ")
    vtelefone = input("Digite o telefone do contato: ")
    vemail = input("Digite o email do contato: ")
    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail = remail
    vsql = "UPDATE tb_contatos SET NOME = '" + vnome + "', TELEFONE = '" + vtelefone + "', EMAIL = '" + vemail + "' WHERE ID = " + vid
    query(vcon, vsql)




def consultarContato():
    pass


def consultarContatoNome():
    pass


while True:
    opt = menuPrincipal()
    if opt == 1:
        # Inserir novo contato
        inserirContato()
    elif opt == 2:
        # Deletar Registro
        deletarContato()
    elif opt == 3:
        # Alterar contato
        alterarContato()
    elif opt == 4:
        # Consultar Registro (ID)
        consultarContato()
    elif opt == 5:
        # Consulta contato (Nome)
        consultarContatoNome()
    elif opt == 6:
        os.system("cls")
        # Sair
        print("Saindo do programa...")
        os.system("pause")
        break
    else:
        os.system("cls")
        print("Opção inválida!")
        os.system("pause")
        continue

vcon.close()
os.system("pause")
