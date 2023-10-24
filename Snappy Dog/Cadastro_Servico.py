import tkinter as TK
from controller import cadastrar_servico,LimparFrame

def Desenhar_cadastro_servico(telapai):
    cadastro_servico=TK.Toplevel(telapai)
    cadastro_servico.geometry("400x250")

    def Enviar_Cadastro_Servico(Tela,nome,descricao,preco):
            cadastrar_servico(nome,descricao,preco)
            LimparFrame(Tela)
    label_servico_nome=TK.Label(cadastro_servico,text='nome do serviço').grid(column=0,row=0)

    entry_servico_nome=TK.Entry(cadastro_servico)
    entry_servico_nome.grid(column=1,row=0)

    label_servico_descricao=TK.Label(cadastro_servico,text='Descricao').grid(column=0,row=1)

    text_servico_descricao=TK.Text(cadastro_servico,width=20,height=5)
    text_servico_descricao.grid(column=1,row=1,pady=10)

    label_servico_preco=TK.Label(cadastro_servico,text='Preço do serviço').grid(column=0,row=2)

    entry_servico_preco=TK.Entry(cadastro_servico)
    entry_servico_preco.grid(column=1,row=2)

    button_servico_enviar=TK.Button(cadastro_servico,text='Enviar',command= 
                                    lambda:Enviar_Cadastro_Servico(cadastro_servico,
                                                                    entry_servico_nome.get(),
                                                                    text_servico_descricao.get("1.0",'end-1c'),
                                                                    entry_servico_preco.get()
                                                                    )).grid(column=0,columnspan=2,row=4)