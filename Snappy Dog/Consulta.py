from tkinter import *
from tkinter import ttk
from view import Cadastro,select_cliente,filtrar_cliente

class janela:
    def __init__(self):
        self.tela=Tk()
        self.tela.state('zoomed')
        self.tela.title('Petshop')
        
        
        self.tela_altura=self.tela.winfo_screenheight()
        self.tela_largura=self.tela.winfo_screenwidth()
    
    def Atualizar_tree_cliente(self,treeview,origem:list):
        treeview.delete(*treeview.get_children())
        for tupla in origem:
            treeview.insert('', END, values=[str(tupla.nome),
                                             (f'({tupla.telefone[0:2]}) {tupla.telefone[2:]}'),
                                             f'{tupla.cpf[0:3]}.{tupla.cpf[3:6]}.{tupla.cpf[6:9]}-{tupla.cpf[9:11]}',
                                             str(tupla.endereco)])

    def desenhar(self):
        #tree view
        tree_collumns=('Nome','Telefone','CPF','Endereço')
        tree=ttk.Treeview(self.tela,columns=tree_collumns
                          ,show='headings',height=self.tela_altura
        )
        
        for x in tree_collumns:
            tree.column(x,width=round(self.tela_largura/len(tree_collumns)))
            tree.heading(x,text=x)

        self.Atualizar_tree_cliente(tree,select_cliente())
        #tela
        tree.grid(row=3,column=0,pady=100,columnspan=4)
        cx_pesquisa=Entry(self.tela,width=100)
        cx_pesquisa.grid(row=0,column=0,columnspan=3,pady=20)

        tipo_pesquisa=ttk.Combobox(self.tela,values=['nome','cpf','telefone'],width=20)
        tipo_pesquisa.grid(row=0,column=2)

        btn_pesquisar=Button(self.tela,width=20,text='Pesquisar',command= lambda:
                             self.Atualizar_tree_cliente(tree,
                                                         filtrar_cliente(cx_pesquisa.get(),tipo_pesquisa.get())
                                                         )).grid(row=0,column=3)

        btn_criar=Button(self.tela,command=lambda:Cadastro(self.tela),text='Cadastrar',width=20).grid(row=1,column=1)
        
        
        btn_Atualizar=Button(self.tela,width=20,text='Atualizar',command=lambda:self.Atualizar_tree_cliente(tree,select_cliente())).grid(row=1,column=0)

        self.tela.mainloop()


janela1=janela().desenhar()

