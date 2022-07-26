import sqlite3
from sqlite3 import Error
import os

caminho = "dados/dados.db"


# criando conexao com o banco de dados
def conexaoBanco(cam):
    try:
        conexao = sqlite3.connect(cam)
        return conexao
    except Error as e:
        print(e)
        return None


# conectao com o banco de dados
vcon = conexaoBanco(caminho)


# inserindo dados no banco de dados
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


# consultando dados no banco de dados
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


# Menu de opções
def menuPrincial():
    try:
        print("""
        1 - Adicionar Tarefa
        2 - Ver Tarefas
        3 - Remover Tarefa
        4 - Alterar Tarefa
        5 - Sair""")
        return input("Digite a opção desejada: ")
    except ValueError:
        print("Opção inválida!")
        return 0


# Inserindo dados no banco de dados
def inserirDados():
    os.system('cls')
    print("Digite o seu nome: ")
    vnome = input()
    print("Digite o seu sobrenome: ")
    vsobrenome = input()
    print("Digite qual a tarefa: ")
    vtarefa = input()
    print("Digite a data do tarefa (yyyy-mm-dd): ")
    vdata = input()
    print("Digite a hora do tarefa (hh:mm): ")
    vhora = input()
    print("Digite o local do tarefa: ")
    vlocal = input()
    print("Digite o tipo do tarefa: ")
    vtipo = input()
    print("Digite a descrição do tarefa: ")
    vdescricao = input()
    print("Digite o status do tarefa: ")
    vstatus = input()
    print("Digite o responsavel do tarefa: ")
    vresponsavel = input()
    vsql = "INSERT INTO agenda (NOME, SOBRENOME, TAREFA, DATA_EVENTO, HORA_EVENTO, LOCAL, TIPO, DESCRICAO, STATUS, RESPONSAVEL) VALUES ('" + vnome + "', '" + vsobrenome + "', '" + vtarefa + "', '" + vdata + "', '" + vhora + "', '" + vlocal + "', '" + vtipo + "', '" + vdescricao + "', '" + vstatus + "', '" + vresponsavel + "')"
    query(vcon, vsql)


# Menu de Tarefas
def MenuTarefas():
    try:
        print("""
         0 - Voltar
         1 - Tarefas Pendentes
         2 - Tarefas Concluidas
         3 - Tarefas Canceladas
         4 - Pelo Nome
         5 - Pelo Responsavel
         6 - Pela Data
         7 - Pela Hora
         8 - Pela Local
         9 - Pela Descrição
        10 - Pela Tipo
        """)
        return input("Digite a opção desejada: ")
    except ValueError:
        print("Opção inválida!")
        return 0


# Consultando dados no banco de dados (STATUS)
def consultarStatus(opt):
    global vsql
    if opt == "1":
        vsql = "SELECT * FROM agenda WHERE STATUS LIKE 'PENDENTE'"
    elif opt == "2":
        vsql = vsql = "SELECT * FROM agenda WHERE STATUS = 'CONCLUIDA' or STATUS = 'pronto' or STATUS ='CONCLUIDO'"
    elif opt == "3":
        vsql = "SELECT * FROM agenda WHERE STATUS = 'CANCELADA 'or STATUS = 'CANCELADO'"
    elif opt == "4":
        print("Digite o nome: ")
        vnome = input()
        vsql = "SELECT * FROM agenda WHERE NOME LIKE '%" + vnome + "%'"
    elif opt == "5":
        print("Digite o responsavel: ")
        vresponsavel = input()
        vsql = "SELECT * FROM agenda WHERE RESPONSAVEL LIKE '%" + vresponsavel + "%'"
    elif opt == "6":
        print("Digite a data: xx/xx/xxxx")
        vdata = input()
        vsql = "SELECT * FROM agenda WHERE DATA_EVENTO LIKE '%" + vdata + "%'"
    elif opt == "7":
        print("Digite a hora: xx:xx")
        vhora = input()
        vsql = "SELECT * FROM agenda WHERE HORA_EVENTO LIKE '%" + vhora + "%'"
    elif opt == "8":
        print("Digite o local: ")
        vlocal = input()
        vsql = "SELECT * FROM agenda WHERE LOCAL LIKE '%" + vlocal + "%'"
    elif opt == "9":
        print("Digite a descrição: ")
        vdescricao = input()
        vsql = "SELECT * FROM agenda WHERE DESCRICAO LIKE '%" + vdescricao + "%'"
    elif opt == "10":
        print("Digite o tipo: ")
        vtipo = input()
        vsql = "SELECT * FROM agenda WHERE TIPO LIKE '%" + vtipo + "%'"
    else:
        print("Opção inválida!")
        return 0
    for i in consultar(vcon, vsql):
        print(
            f'ID: {i[0]}\nNome: {i[1]}\nSobrenome: {i[2]}\nTarefa: {i[3]}\nData: {i[4]}\nHora: {i[5]}\nLocal: {i[6]}\nTipo: {i[7]}\nDescrição: {i[8]}\nStatus: {i[9]}\nResponsavel: {i[10]}')
        print("\n")




if __name__ == "__main__":
    while True:
        opcao = menuPrincial()
        if opcao == "1":
            inserirDados()
        elif opcao == "2":
            opt = MenuTarefas()
            if opt == '1':
                print("Tarefas Pendentes")
                consultarStatus(opt)
            elif opt == '2':
                print("Tarefas Concluidas")
                consultarStatus(opt)
            elif opt == '3':
                print("Tarefas Canceladas")
                consultarStatus(opt)
            elif opt == '4':
                print("Pelo Nome")
                consultarStatus(opt)
            elif opt == '5':
                print("Pelo Responsavel")
                consultarStatus(opt)
            elif opt == '6':
                print("Pela Data")
                consultarStatus(opt)
            elif opt == '7':
                print("Pela Hora")
                consultarStatus(opt)
            elif opt == '8':
                print("Pela Local")
                consultarStatus(opt)
            elif opt == '9':
                print("Pela Descrição")
                consultarStatus(opt)
            elif opt == '10':
                print("Pela Tipo")
                consultarStatus(opt)
            elif opt == '0':
                print("Voltando ao menu principal")
                continue
            else:
                print(f"opção digita foi {opt}")
                print("Opção inválida!")
                continue
