import tkinter as TK
from controller import cadastrar_servico,Atualizar_tree_servico,select_servico,atualizar_servico

def Desenhar_cadastro_servico(telapai,tree,update=False,servico=object):
        cadastro_servico=TK.Toplevel(telapai)
        cadastro_servico.geometry("400x250")

        def Enviar_Cadastro_Servico(nome,preco,descricao):
                if update:
                        if atualizar_servico(nome,preco,descricao,servico):
                                cadastro_servico.destroy()
                                Atualizar_tree_servico(tree,select_servico())
                else:
                        if cadastrar_servico(nome,preco,descricao):
                                cadastro_servico.destroy()
                                Atualizar_tree_servico(tree,select_servico())

        label_servico_nome=TK.Label(cadastro_servico,text='nome do serviço').grid(column=0,row=0)

        entry_servico_nome=TK.Entry(cadastro_servico)
        entry_servico_nome.grid(column=1,row=0)

        label_servico_preco=TK.Label(cadastro_servico,text='Preço do serviço').grid(column=0,row=1)

        entry_servico_preco=TK.Entry(cadastro_servico)
        entry_servico_preco.grid(column=1,row=1)
        label_servico_descricao=TK.Label(cadastro_servico,text='Descricao').grid(column=0,row=2)

        text_servico_descricao=TK.Text(cadastro_servico,width=20,height=5)
        text_servico_descricao.grid(column=1,row=2,pady=10)

    

        button_servico_enviar=TK.Button(cadastro_servico,text='Enviar',command= 
                                    lambda:Enviar_Cadastro_Servico(
                                                                    entry_servico_nome.get(),
                                                                    entry_servico_preco.get(),
                                                                    text_servico_descricao.get("1.0",'end-1c')
                                                                    )).grid(column=0,columnspan=2,row=4)
        if update:
                entry_servico_nome.insert(0,servico.nome)
                entry_servico_preco.insert(0,servico.preco)
                text_servico_descricao.insert('1.0',servico.nome)