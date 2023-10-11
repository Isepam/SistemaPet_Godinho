from tkinter import *
from tkinter import ttk
from view import Cadastro,select_cliente

class janela:
    def __init__(self):
        self.tela=Tk()
        self.tela.state('zoomed')

        
        self.tela_altura=self.tela.winfo_screenheight()
        self.tela_largura=self.tela.winfo_screenwidth()
    def Atualizar_cliente(self,treeview):
        tuplas=select_cliente()
        treeview.delete(*treeview.get_children())
        for tupla in tuplas:
            treeview.insert('', END, values=tupla)

    def desenhar(self):
        #tree view
        tree_collumns=('Nome','Telefone','CPF','Endereço')
        tree=ttk.Treeview(self.tela,columns=tree_collumns
                          ,show='headings',height=self.tela_altura
        )
        
        for x in tree_collumns:
            tree.column(x,width=round(self.tela_largura/len(tree_collumns)))
            tree.heading(x,text=x)
        #tela
        tree.grid(row=3,column=0,pady=100,columnspan=2)

        btn_criar=Button(self.tela,command=lambda:Cadastro(self.tela),text='Cadastrar',width=20).grid(row=1,column=1)
        cx_pesquisa=Entry(self.tela,width=200)
        cx_pesquisa.grid(row=0,column=0)
        btn_pesquisa=Button(self.tela,width=20,text='Atualizar',command=self.Atualizar_cliente(tree)).grid(row=2,column=1)

        self.tela.mainloop()


janela1=janela().desenhar()

