from tkinter import *
import os

caminho = os.path.dirname(__file__)
nomeArquivo = caminho + '/dados.txt'


def grava_dados():
    arquivo = open(caminho + '/dados.txt', 'a', encoding='utf-8')
    arquivo.write(f"Nome......:{vnome.get()} \n")
    arquivo.write(f"Sobrenome.:{vsobrenome.get()} \n")
    arquivo.write(f"E-mail....:{vemail.get()} \n")
    arquivo.write(f"Telefone..:{vtelefone.get()} \n")
    arquivo.write(f"Observação:{obs.get('1.0', 'end-1c')} \n")
    arquivo.write("\n")
    arquivo.close()
    print("Botao clicado")
    vnome.delete(0, END)
    vsobrenome.delete(0, END)
    vemail.delete(0, END)
    vtelefone.delete(0, END)
    obs.delete(1.0, END)


app = Tk()

app.title("Tkinter")
app.geometry("500x350")
app.configure(background='#dde')

lb1 = Label(app, text="Nome", bg='#dde', fg='#009', anchor='w')
lb1.place(x=10, y=10, width=100, height=20)
vnome = Entry(app, width=30)
vnome.place(x=10, y=30, width=100, height=20)

lb2 = Label(app, text="Sobrenome", bg='#dde', fg='#009', anchor='w')
lb2.place(x=10, y=60, width=100, height=20)
vsobrenome = Entry(app, width=30)
vsobrenome.place(x=10, y=80, width=100, height=20)

lb3 = Label(app, text="E-mail", bg='#dde', fg='#009', anchor='w')
lb3.place(x=10, y=110, width=100, height=20)
vemail = Entry(app, width=30)
vemail.place(x=10, y=130, width=200, height=20)

lb4 = Label(app, text="Telefone", bg='#dde', fg='#009', anchor='w')
lb4.place(x=10, y=160, width=100, height=20)
vtelefone = Entry(app, width=30)
vtelefone.place(x=10, y=180, width=150, height=20)

lb5 = Label(app, text="Observação", bg='#dde', fg='#009', anchor='w')
lb5.place(x=10, y=210, width=100, height=20)
obs = Text(app, width=30, height=5)
obs.place(x=10, y=230, width=300, height=60)

Button(app, text="Salvar", command=grava_dados).place(x=10, y=300, width=100, height=20)

app.mainloop()
