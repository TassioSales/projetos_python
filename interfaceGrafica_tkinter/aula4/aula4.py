from tkinter import *
import banco
import os

caminho = os.path.dirname(__file__)
nomeArquivo = caminho + '/dados.txt'

def GravaDados():
    if tb_nome.get() != "":
        vnome = tb_nome.get()
        vsobrenome = tb_sobrenome.get()
        vemail = tb_email.get()
        vtelefone = tb_telefone.get()
        obs = tb_obs.get('1.0', 'end-1c')
        vquery = f"INSERT INTO tb_contatos (NOME, TELEFONE, EMAIL, SOBRENOME, OBS) VALUES ('{vnome}', '{vsobrenome}', '{vemail}', '{vtelefone}', '{obs}')"
        banco.dml(vquery)
        tb_nome.delete(0, END)
        tb_sobrenome.delete(0, END)
        tb_email.delete(0, END)
        tb_telefone.delete(0, END)
        tb_obs.delete(1.0, END)
        print("Gravando dados")
    else:
        print("Não gravou")



def grava_dados():
    arquivo = open(caminho + '/dados.txt', 'a', encoding='utf-8')
    arquivo.write(f"Nome......:{tb_nome.get()} \n")
    arquivo.write(f"Sobrenome.:{tb_sobrenome.get()} \n")
    arquivo.write(f"E-mail....:{tb_email.get()} \n")
    arquivo.write(f"Telefone..:{tb_telefone.get()} \n")
    arquivo.write(f"Observação:{tb_obs.get('1.0', 'end-1c')} \n")
    arquivo.write("\n")
    arquivo.close()
    print("Botao clicado")
    tb_nome.delete(0, END)
    tb_sobrenome.delete(0, END)
    tb_email.delete(0, END)
    tb_telefone.delete(0, END)
    tb_obs.delete(1.0, END)


app = Tk()

app.title("Tkinter")
app.geometry("500x350")
app.configure(background='#dde')

lb1 = Label(app, text="Nome", bg='#dde', fg='#009', anchor='w')
lb1.place(x=10, y=10, width=100, height=20)
tb_nome = Entry(app, width=30)
tb_nome.place(x=10, y=30, width=100, height=20)

lb2 = Label(app, text="Sobrenome", bg='#dde', fg='#009', anchor='w')
lb2.place(x=10, y=60, width=100, height=20)
tb_sobrenome = Entry(app, width=30)
tb_sobrenome.place(x=10, y=80, width=100, height=20)

lb3 = Label(app, text="E-mail", bg='#dde', fg='#009', anchor='w')
lb3.place(x=10, y=110, width=100, height=20)
tb_email = Entry(app, width=30)
tb_email.place(x=10, y=130, width=200, height=20)

lb4 = Label(app, text="Telefone", bg='#dde', fg='#009', anchor='w')
lb4.place(x=10, y=160, width=100, height=20)
tb_telefone = Entry(app, width=30)
tb_telefone.place(x=10, y=180, width=150, height=20)

lb5 = Label(app, text="Observação", bg='#dde', fg='#009', anchor='w')
lb5.place(x=10, y=210, width=100, height=20)
tb_obs = Text(app, width=30, height=5)
tb_obs.place(x=10, y=230, width=300, height=60)

Button(app, text="Salvar TXT", command=grava_dados).place(x=10, y=300, width=100, height=20)
Button(app, text="Salvar DB", command=GravaDados).place(x=120, y=300, width=100, height=20)

app.mainloop()