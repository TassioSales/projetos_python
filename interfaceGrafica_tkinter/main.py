from tkinter import *

app = Tk()
app.title("Tkinter")
app.geometry("500x300")
app.configure(background='#008')

txt1 = Label(app, text="Hello World", bg='#008', fg='#fff')
txt1.place(x=10, y=10, width=150, height=50)

vtxt1 = 'Modulo Tkinter'
vbg = '#008'
vfg = '#fff'
txt2 = Label(app, text=vtxt1, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=10, pady=10, side="top", fill=X, expand=True)

app.mainloop()
