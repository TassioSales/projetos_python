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
    try:
        os.system("cls")
        print("""
        1 - Inserir novo contato
        2 - Deletar Registro
        3 - Alterar contato
        4 - Consultar Registros
        5 - Consulta contato (Nome)
        6 - Sair""")
        opcao = int(input("Digite a opção desejada: "))
        return opcao
    except ValueError:
        print("Opção inválida!")
        return 0


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
    resp = consultar(vcon, "SELECT * FROM tb_contatos WHERE ID = " + vid)
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
    os.system("cls")
    cont = 0
    vslq = "SELECT * FROM tb_contatos"
    for i in consultar(vcon, vslq):
        print(f'ID:  {i[0]:_<3}, Nome: , {i[1]:_<30}, Telefone: , {i[2]:_<14}, Email: , {i[3]:_<30}')
        cont += 1
        if cont == 10:
            resp = input("Deseja continuar? (S/N) ").upper().strip()[0]
            if resp == "S":
                os.system("pause")
                os.system("cls")
                cont = 0
            else:
                break
    print(f"Total de {cont} registros")
    print("Fim da lista")
    os.system("pause")


def consultarContatoNome():
    os.system("cls")
    cont = 0
    vnome = input("Digite o nome do contato: ")
    vsql = "SELECT * FROM tb_contatos WHERE NOME LIKE '%" + vnome + "%'"
    resp = consultar(vcon, vsql)
    for i in resp:
        print(f'ID:  {i[0]:_<3}, Nome: , {i[1]:_<30}, Telefone: , {i[2]:_<14}, Email: , {i[3]:_<30}')
        cont += 1
        if cont == 10:
            resp = input("Deseja continuar? (S/N) ").upper().strip()[0]
            if resp == "S":
                os.system("pause")
                os.system("cls")
                cont = 0
            else:
                break
    print(f"Total de {cont} registros")
    print("Fim da lista")
    os.system("pause")


if __name__ == "__main__":
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
        elif opt == 0:
            os.system("cls")
            os.system("pause")
        else:
            os.system("cls")
            print("Opção inválida!")
            os.system("pause")
            continue

    vcon.close()
    os.system("pause")
