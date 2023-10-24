from tkinter import *
from tkinter import ttk
from controller import select_cliente,filtrar_cliente
from Cadastro_Cliente import Desenhar_cadastro_cliente
from Cadastro_Animal import Desenhar_cadastro_animal

class janela_cliente:
    def __init__(self):
        self.tela=Tk()
        self.tela.state('zoomed')
        self.tela.title('Petshop')   
        
        
        self.tela_altura=self.tela.winfo_screenheight()
        self.tela_largura=self.tela.winfo_screenwidth()
    
    def Atualizar_tree_cliente(self,treeview,origem:list):
        treeview.delete(*treeview.get_children())
        for tupla in origem:
            treeview.insert('', END, values=[str(tupla),
                                             str(tupla.nome),
                                             str(f'({tupla.telefone[0:2]}) {tupla.telefone[2:]}'),
                                             str(f'{tupla.cpf[0:3]}.{tupla.cpf[3:6]}.{tupla.cpf[6:9]}-{tupla.cpf[9:11]}'),
                                             str(tupla.endereco)])

    def desenhar(self):
        #tree view
        tree_collumns=('Id','Nome','Telefone','CPF','Endereço')
        tree=ttk.Treeview(self.tela,columns=tree_collumns
                          ,show='headings',height=self.tela_altura
        )
        tree_collumns_wid=(1,2,2,2,3)

        for text,wid in zip(tree_collumns,tree_collumns_wid):
            tree.column(text,width=round((self.tela_largura/sum(tree_collumns_wid))*wid ))
            tree.heading(text,text=text)

        tree.bind('<<TreeviewOpen>>',self.Atualizar_tree_cliente(tree,select_cliente()))
        #tela



        cx_pesquisa=Entry(self.tela,width=100)
        cx_pesquisa.grid(row=0,column=0,columnspan=2,pady=20,sticky=E)

        tipo_pesquisa=ttk.Combobox(self.tela,values=['nome','cpf','telefone'],width=20)
        tipo_pesquisa.grid(row=0,column=2,sticky=W)

        btn_pesquisar=Button(self.tela,width=20,text='Pesquisar',command= lambda:
                             self.Atualizar_tree_cliente(tree,
                                                         filtrar_cliente(cx_pesquisa.get(),tipo_pesquisa.get())
                                                         )).grid(row=0,column=3,sticky=W)


        # Botões
        
        btn_Atualizar=Button(self.tela,width=20,text='Atualizar',command=
                             lambda:self.Atualizar_tree_cliente(tree,select_cliente()
                                                                )).grid(row=1,column=0)
        
        btn_criar=Button(self.tela,width=20,text='Cadastrar',command=
                         lambda:Desenhar_cadastro_animal(self.tela)
                         ).grid(row=1,column=1)
        
        btn_Editar=Button(self.tela,width=20,text='Editar'
                          ).grid(row=1,column=2)
        #View
        tree.grid(row=3,column=0,pady=100,columnspan=4)

        self.tela.mainloop()


janela_cliente().desenhar()

