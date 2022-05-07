from tkinter import *
from tkinter import messagebox


def telinha():
    jan = Tk()
    jan.geometry("500x300")
    jan.configure(background="#dde")

    Label(jan, text="numero_um", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100,
                                                                                       height=20)

    vnum_um = Entry(jan)
    vnum_um.place(x=10, y=30, width=50, height=20)

    Label(jan, text="numero_dois", background="#dde", foreground="#009", anchor=W).place(x=100, y=10, width=100,
                                                                                         height=20)
    vnum_dois = Entry(jan)
    vnum_dois.place(x=100, y=30, width=50, height=20)

    def soma_numero():
        soma = int(vnum_um.get()) + int(vnum_dois.get())
        messagebox.showinfo(title="Soma", message=f"{vnum_um.get()} + {vnum_dois.get()} = {soma}")

    def subtrair_numero():
        sub = int(vnum_um.get()) - int(vnum_dois.get())
        messagebox.showinfo(title="Subtração", message=f"{vnum_um.get()} - {vnum_dois.get()} = {sub}")

    Button(jan, text="Soma", command=soma_numero).place(x=10, y=120, width=100, height=20)
    Button(jan, text="Sobtração", command=subtrair_numero).place(x=10, y=150, width=100, height=20)

    jan.mainloop()


if __name__ == '__main__':
    telinha()
