from tkinter import *
from tkinter import messagebox
import random

sorteados = random.randrange(0, 10)
erros = 0


def telinha():
    def adivinha_numero():

        if int(vnumero.get()) > sorteados:
            messagebox.showinfo(title="Erro", message=f"Erro numero e menor")

        elif int(vnumero.get()) < sorteados:
            messagebox.showinfo(title="Erro", message=f"Erro numero e maior")

        else:
            messagebox.showinfo(title="Acertou", message=f"O numero era {sorteados}")

    jan = Tk()
    jan.geometry("200x150")
    jan.configure(background="#dde")

    Label(jan, text="numero_um", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100,
                                                                                       height=20)
    vnumero = Entry(jan)
    vnumero.place(x=10, y=30, width=50, height=20)

    Button(jan, text="adivinha", command=adivinha_numero).place(x=10, y=120, width=100, height=20)

    jan.mainloop()


if __name__ == '__main__':
    telinha()
