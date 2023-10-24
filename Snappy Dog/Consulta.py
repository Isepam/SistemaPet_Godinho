from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller import select_cliente,filtrar_cliente,Atualizar_tree_cliente,Apagar_Instancia
from Cadastro_Cliente import Desenhar_cadastro_cliente

class janela_cliente:
    def __init__(self):
        self.tela=Tk()
        self.tela.state('zoomed')
        self.tela.title('Petshop')   
        
        self.tela_altura=self.tela.winfo_screenheight()
        self.tela_largura=self.tela.winfo_screenwidth()

    def Apagar_cliente(self,tree):
        resposta=messagebox.askokcancel('Apagar','Tem certeza que deseja apagar esse cliente')
        if resposta:
            for sitem in tree.selection():
                item=tree.item(sitem)
                Apagar_Instancia(int(item['values'][0]),'Cliente',tree)
        
    


    def desenhar(self):
        #tree view
        frame_treeview=Frame(self.tela)
        tree_collumns=('Id','Nome','Telefone','CPF','Endereço')
        tree=ttk.Treeview(frame_treeview,columns=tree_collumns
                          ,show='headings',height=self.tela_altura
        )
        tree_collumns_wid=(10,20,20,20,30,10)

        for text,wid in zip(tree_collumns,tree_collumns_wid):
            tree.column(text,width=round((self.tela_largura/sum(tree_collumns_wid))*wid ))
            tree.heading(text,text=text)

        scrollbar = ttk.Scrollbar(frame_treeview, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        

        tree.bind('<<TreeviewOpen>>',Atualizar_tree_cliente(tree,select_cliente()))
        #tela


        cx_pesquisa=Entry(self.tela,width=100)
        cx_pesquisa.grid(row=0,column=0,columnspan=2,pady=20,sticky=E)

        
        frame_pesquisa=Frame(self.tela)
        tipo_pesquisa=ttk.Combobox(frame_pesquisa,values=['nome','cpf','telefone'],width=20)
        tipo_pesquisa.grid(row=0,column=0)

        btn_pesquisar=Button(frame_pesquisa,width=20,text='Pesquisar',command= lambda:
                             Atualizar_tree_cliente(tree,
                                                         filtrar_cliente(cx_pesquisa.get(),tipo_pesquisa.get())
                                                         )).grid(row=0,column=1)
        frame_pesquisa.grid(row=0,column=2,sticky=W)

        # Botões 
        btn_criar=Button(self.tela,width=20,text='Cadastrar',command=
                         lambda:Desenhar_cadastro_cliente(self.tela,tree)
                         ).grid(row=1,column=0)
        
        btn_Editar=Button(self.tela,width=20,text='Editar'
                          ).grid(row=1,column=1)
        
        btn_Apagar=Button(self.tela,width=20,text='Apagar',command= 
                          lambda: self.Apagar_cliente(tree)
                          ).grid(row=1,column=2)
        #View
        frame_treeview.grid(row=3,column=0,columnspan=4,pady=50)
        tree.grid(row=0,column=0)
        scrollbar.grid(row=0,column=1)

        self.tela.mainloop()


janela_cliente().desenhar()

