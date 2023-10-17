from tkinter import *
from tkinter import ttk
class login:
    def __init__(self,telapai):
        self.tela=telapai
        self.tela.geometry('350x250')
    def desenhar(self):
        note= ttk.Notebook(self.tela)
        frame_login=Frame(note)
        frame_cadastro=Frame(note)
        note.add(frame_login,text="Login")
        note.add(frame_cadastro,text="Cadastro")

        label_nome=Label(frame_login,text="Nome").grid(row=0,column=0,sticky='w')
        Entry_nome=Entry(frame_login,width=50)
        Entry_nome.grid(row=1,column=0,pady=20)

        label_senha=Label(frame_login,text="Senha").grid(row=2,column=0,sticky='w')
        Entry_senha=Entry(frame_login,width=50)
        Entry_senha.grid(row=3,column=0,pady=20)

        btn_Login=Button(frame_login,text='Logar').grid(row=4,column=0)
        note.pack(expand=True,fill=BOTH)
        self.tela.mainloop()
root= Tk()
login1=login(root)
login1.desenhar()