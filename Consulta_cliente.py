from tkinter import *
from tkinter import ttk
from controller import *
from Cadastro_Cliente import Desenhar_cadastro_cliente



class janela_cliente:
    def __init__(self):
        self.tela=Tk()
        self.tela.state('zoomed')
        self.tela.title('Petshop') 
        self.tela_altura=self.tela.winfo_screenheight()
        self.tela_largura=self.tela.winfo_screenwidth()

    def Apagar_cliente(self,tree):
        resposta=messagebox.askokcancel('Apagar','Tem certeza que deseja apagar esse cliente(s)')
        if resposta:
            for sitem in tree.selection():
                print(sitem)
                item=tree.item(sitem)
                Apagar_Instancia(int(item['values'][0]),'Cliente')
            Atualizar_tree_cliente(tree,select_cliente())

    def Update_cliente(self,tree):
        for sitem in tree.selection():
            item=tree.item(sitem)
            Desenhar_cadastro_cliente(self.tela,tree,True,filtrar_cliente(item['values'][0]))

    def desenhar(self):
        #tree view-----------------------------------

        #frame

        frame_treeview=Frame(self.tela)

        #criação da Tree:

        tree_collumns=('Id','Nome','Telefone','CPF','Endereço')
        tree=ttk.Treeview(frame_treeview,columns=tree_collumns
                          ,show='headings',height=27
        )

        #tamnho para cada coluna

        tree_collumns_wid=(10,20,20,20,30)

        for text,wid in zip(tree_collumns,tree_collumns_wid):
            tree.column(text,width=round(((self.tela_largura*0.985)/sum(tree_collumns_wid))*wid ))
            tree.heading(text,text=text)
        
        #atualização quando abre

        tree.bind('<<TreeviewOpen>>',Atualizar_tree_cliente(tree,select_cliente()))

        #scrollbar

        scrollbar = ttk.Scrollbar(frame_treeview, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)

        #Desenho de tela-------------------------------------------------


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
        
        btn_Editar=Button(self.tela,width=20,text='Editar',command=
                          lambda: self.Update_cliente(tree)
                          ).grid(row=1,column=1)
        
        btn_Apagar=Button(self.tela,width=20,text='Apagar',command= 
                          lambda: self.Apagar_cliente(tree)
                          ).grid(row=1,column=2)
        #View
        frame_treeview.grid(row=3,column=0,columnspan=4,pady=50)
        tree.grid(row=0,column=0)
        scrollbar.grid(row=0,column=1)
        #main loop
        self.tela.mainloop()

janela_cliente().desenhar()

        


