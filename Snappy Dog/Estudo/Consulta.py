from tkinter import *
from tkinter import ttk

class janela:
    def __init__(self):
        self.tela=Tk()
        self.tela.attributes('-fullscreen',True)
        
        self.tela_altura=self.tela.winfo_screenheight()
        self.tela_largura=self.tela.winfo_screenwidth()
    def desenhar(self):
        tree_collumns=('Nome','Telefone','CPF')
        tree=ttk.Treeview(self.tela,columns=tree_collumns
                          ,show='headings',height=self.tela_altura
        )
        
        for x in tree_collumns:
            tree.column(x,width=round(self.tela_largura/len(tree_collumns)))
            tree.heading(x,text=x)

        tree.grid(row=0,column=0,pady=100)

        self.tela.mainloop()


janela1=janela()
janela1.desenhar()
