from tkinter import *


def imprime_dados():
    print("Hello Word")
    print(f"Olá {vmensagem.get()}")


root = Tk()
root.geometry("500x300")
root.configure(background="#dde")

Label(root, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
vmensagem = Entry(root)
vmensagem.place(x=10, y=50, width=200, height=20)

Button(root, text="imprimir", command=imprime_dados).place(x=10, y=100, width=100, height=20)
root.mainloop()
