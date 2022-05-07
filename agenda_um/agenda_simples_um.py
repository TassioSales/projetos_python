from tkinter import *
from tkinter import messagebox


def agenda():
    def imprime_dados():
        nome = f"NOME....: {vnome.get()}"
        telefone = f"TELEFONE: {vtelefone.get()}"
        email = f'EMAIL...: {vemail.get()}'
        obs = f"OBS.....: {vobs.get('1.0', END)}"
        messagebox.showinfo(title="DADOS", message=f"{nome} \n {telefone} = \n {email} \n {obs}")

    app_agenda = Tk()
    app_agenda.geometry("500x300")
    app_agenda.configure(background="#dde")

    Label(app_agenda, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100,
                                                                                         height=20)
    vnome = Entry(app_agenda)
    vnome.place(x=10, y=30, width=200, height=20)

    Label(app_agenda, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=100,
                                                                                             height=20)
    vtelefone = Entry(app_agenda)
    vtelefone.place(x=10, y=80, width=100, height=20)

    Label(app_agenda, text="Email", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=100,
                                                                                          height=20)
    vemail = Entry(app_agenda)
    vemail.place(x=10, y=130, width=300, height=20)

    Label(app_agenda, text="OBS", background="#dde", foreground="#009", anchor=W).place(x=10, y=160, width=100,
                                                                                        height=20)
    vobs = Text(app_agenda)
    vobs.place(x=10, y=180, width=300, height=80)

    Button(app_agenda, text="imprimir", command=imprime_dados).place(x=10, y=270, width=100, height=20)

    app_agenda.mainloop()


def mostra_tela():
    return agenda()


if __name__ == '__main__':
    agenda()
