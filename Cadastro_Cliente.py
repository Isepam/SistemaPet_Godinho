import tkinter as TK
from controller import cadastrar_cliente,Atualizar_cliente,Atualizar_tree_cliente,select_cliente
def Desenhar_cadastro_cliente(telapai,treeview,update=False,cliente=object):
    cadastro_cliente=TK.Toplevel(telapai)
    cadastro_cliente.geometry("400x250")

    def Enviar_Cadastro_Cliente(Nome:str,telefone:str,cpf:str,endereco:str):
        if update:
            if Atualizar_cliente(Nome,telefone,cpf,endereco,cliente):
                cadastro_cliente.destroy()
                Atualizar_tree_cliente(treeview,select_cliente())
        else:
            if cadastrar_cliente(Nome,telefone,cpf,endereco):
                cadastro_cliente.destroy()
                Atualizar_tree_cliente(treeview,select_cliente())
    #cadrasto Cliente
    label_cliente_nome=TK.Label(cadastro_cliente,text='Nome').grid(column=0,row=0)

    entry_cliente_nome=TK.Entry(cadastro_cliente)
    entry_cliente_nome.grid(column=1,row=0,pady=10)

    label_cliente_telefone=TK.Label(cadastro_cliente,text='Telefone').grid(column=0,row=1)

    entry_cliente_telefone=TK.Entry(cadastro_cliente)
    entry_cliente_telefone.grid(column=1,row=1,pady=10)

    label_cliente_cpf=TK.Label(cadastro_cliente,text='CPF').grid(column=0,row=2)

    entry_cliente_cpf=TK.Entry(cadastro_cliente)
    entry_cliente_cpf.grid(column=1,row=2,pady=10)

    label_cliente_endereco=TK.Label(cadastro_cliente,text='Endereço').grid(column=0,row=3)

    text_cliente_endereco=TK.Text(cadastro_cliente,width=20,height=2)
    text_cliente_endereco.grid(column=1,row=3,pady=10,columnspan=3)

    button_cliente_enviar=TK.Button(cadastro_cliente,text='Enviar',command=
                        lambda: Enviar_Cadastro_Cliente(cadastro_cliente,
                                                        entry_cliente_nome.get(),
                                                        entry_cliente_telefone.get(),
                                                        entry_cliente_cpf.get(),
                                                        text_cliente_endereco.get("1.0",'end-1c')
                                                        )).grid(column=0,columnspan=2,row=4,pady=10)
    if update:
        entry_cliente_nome.insert(0,cliente.nome)
        entry_cliente_telefone.insert(0,cliente.telefone)
        entry_cliente_cpf.insert(0,cliente.cpf)
        text_cliente_endereco.insert('1.0',cliente.endereco)