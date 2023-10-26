from tkinter import *
from tkinter import ttk
from controller import *
from Cadastro_Cliente import Desenhar_cadastro_cliente
from Cadastro_Animal import Desenhar_cadastro_animal

root=Tk()
root.state('zoomed')
root.title('Petshop')  


class janela_cliente:
    def __init__(self,frame):
        self.tela=frame
        self.tela_altura=root.winfo_screenheight()
        self.tela_largura=root.winfo_screenwidth()

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
        tree_collumns_wid=(10,20,20,20,30,1)

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


#Animal:

class janela_Animal:
    def __init__(self,frame):
        self.tela=frame
        self.tela_altura=root.winfo_screenheight()
        self.tela_largura=root.winfo_screenwidth()

    def Apagar_cliente(self,tree):
        resposta=messagebox.askokcancel('Apagar','Tem certeza que deseja apagar esse Pet')
        if resposta:
            for sitem in tree.selection():
                item=tree.item(sitem)
                Apagar_Instancia(int(item['values'][0]),'Animal',tree)
        
    


    def desenhar(self):
        #tree view
        frame_treeview=Frame(self.tela)
        tree_collumns=('Id','Nome','Especie','Raça','Porte','Dono')
        tree=ttk.Treeview(frame_treeview,columns=tree_collumns
                          ,show='headings',height=self.tela_altura
        )
        tree_collumns_wid=(10,20,20,20,20,20,1)

        for text,wid in zip(tree_collumns,tree_collumns_wid):
            tree.column(text,width=round((self.tela_largura/sum(tree_collumns_wid))*wid ))
            tree.heading(text,text=text)

        scrollbar = ttk.Scrollbar(frame_treeview, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        

        tree.bind('<<TreeviewOpen>>',Atualizar_tree_animal(tree,select_animal()))
        #tela


        cx_pesquisa=Entry(self.tela,width=100)
        cx_pesquisa.grid(row=0,column=0,columnspan=2,pady=20,sticky=E)

        
        frame_pesquisa=Frame(self.tela)
        tipo_pesquisa=ttk.Combobox(frame_pesquisa,values=['nome','cpf','telefone'],width=20)
        tipo_pesquisa.grid(row=0,column=0)

        btn_pesquisar=Button(frame_pesquisa,width=20,text='Pesquisar',command= lambda:
                             Atualizar_tree_animal(tree,
                                                         filtrar_cliente(cx_pesquisa.get(),tipo_pesquisa.get())
                                                         )).grid(row=0,column=1)
        frame_pesquisa.grid(row=0,column=2,sticky=W)

        # Botões 
        btn_criar=Button(self.tela,width=20,text='Cadastrar',command=
                         lambda:Desenhar_cadastro_animal(self.tela)
                         ).grid(row=1,column=0)
        
        btn_Editar=Button(self.tela,width=20,text='Editar'
                          ).grid(row=1,column=1)
        
        btn_Apagar=Button(self.tela,width=20,text='Apagar',command= 
                          lambda: self.Apagar_cliente(tree)
                          ).grid(row=1,column=2)
        #View
        tree.grid(row=0,column=0)
        scrollbar.grid(row=0,column=1)
        frame_treeview.grid(row=3,column=0,columnspan=4,pady=50)
        

        
note=ttk.Notebook(root)
note.pack(fill='both',expand=True)

frame_cliente=Frame(note)
frame_cliente.pack(fill='both', expand=True)
frame_animal=Frame(note)
frame_animal.pack(fill='both', expand=True)

view_cliente=janela_cliente(frame_cliente)
view_cliente.desenhar()

view_animais=janela_Animal(frame_animal)
view_animais.desenhar()

note.add(frame_cliente,text="Cliente")
note.add(frame_animal,text="Animais")

root.mainloop()
